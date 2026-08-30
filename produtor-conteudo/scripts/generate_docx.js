#!/usr/bin/env node
/**
 * Renders a quarterly content-strategy plan (JSON) into a .docx that mirrors
 * the structure of the reference plan this skill was built from: a Title,
 * intro sections, one block per month (thematic axis + N "pautas" with a
 * fixed set of strategic fields), and closing sections that tie the quarter
 * together.
 *
 * Usage: node generate_docx.js <input.json> <output.docx>
 *
 * See references/schema.md for the full JSON shape and references/example-plan.json
 * for a worked example.
 */

const fs = require("fs");
const path = require("path");
const {
  Document,
  Packer,
  Paragraph,
  TextRun,
  HeadingLevel,
  AlignmentType,
  LevelFormat,
  ExternalHyperlink,
} = require("docx");

const [, , inputPath, outputPath] = process.argv;

if (!inputPath || !outputPath) {
  console.error("Usage: node generate_docx.js <input.json> <output.docx>");
  process.exit(1);
}

const plan = JSON.parse(fs.readFileSync(inputPath, "utf-8"));

const DEFAULT_LABELS = {
  type: "Tipo:",
  social_headline: "Headline para redes sociais:",
  direcionamento: "Direcionamento:",
  central_question: "Pergunta central:",
  structure: "Estrutura esperada:",
  sources: "Fontes:",
  keywords: "Palavras-chave:",
  tone: "Tom:",
};
const labels = Object.assign({}, DEFAULT_LABELS, plan.labels || {});

const HEADING_BY_LEVEL = {
  1: HeadingLevel.HEADING_1,
  2: HeadingLevel.HEADING_2,
  3: HeadingLevel.HEADING_3,
};

const BULLET_REF = "bullet-list";

function heading(text, level) {
  return new Paragraph({
    heading: HEADING_BY_LEVEL[level] || HeadingLevel.HEADING_2,
    children: [new TextRun({ text })],
  });
}

function body(text) {
  return new Paragraph({ children: [new TextRun({ text })] });
}

function bullet(children) {
  return new Paragraph({
    numbering: { reference: BULLET_REF, level: 0 },
    children,
  });
}

function labeledBullet(label, text) {
  const children = [];
  if (label) {
    children.push(new TextRun({ text: `${label}: `, bold: true }));
    children.push(new TextRun({ text }));
  } else {
    children.push(new TextRun({ text }));
  }
  return bullet(children);
}

function labelLine(label) {
  return new Paragraph({
    children: [new TextRun({ text: label, bold: true })],
  });
}

// A source is {title, publication, year?, url}. Rendered as one bullet with
// a real clickable hyperlink, not a plain-text URL, so the citation is
// actually usable when the plan is reviewed or later turned into a blog post.
function sourceBullet(source) {
  const label = source.year
    ? `${source.title} — ${source.publication} (${source.year})`
    : `${source.title} — ${source.publication}`;
  const children = [new TextRun({ text: `${label}: ` })];
  if (source.url) {
    children.push(
      new ExternalHyperlink({
        link: source.url,
        children: [
          new TextRun({ text: source.url, style: "Hyperlink" }),
        ],
      })
    );
  }
  return bullet(children);
}

// Renders the flexible, freeform section list used for intro/closing content
// (sections_before_months / closing_sections). Each entry may carry a
// heading, plain paragraphs, and/or a bullet list, in any combination.
function renderFreeformSections(sections) {
  const out = [];
  for (const section of sections || []) {
    if (section.heading) {
      out.push(heading(section.heading, section.level || 2));
    }
    for (const p of section.paragraphs || []) {
      out.push(body(p));
    }
    for (const b of section.bullets || []) {
      out.push(labeledBullet(null, b));
    }
  }
  return out;
}

function renderPauta(pauta) {
  const out = [];
  out.push(
    heading(`PAUTA ${pauta.number}: ${pauta.title}`, 2)
  );

  out.push(labelLine(labels.type));
  out.push(body(pauta.type));

  if (pauta.social_headline) {
    out.push(labelLine(labels.social_headline));
    out.push(body(pauta.social_headline));
  }

  out.push(labelLine(labels.direcionamento));
  for (const item of pauta.direcionamento || []) {
    out.push(labeledBullet(item.label, item.text));
  }

  out.push(labelLine(labels.central_question));
  out.push(body(pauta.central_question));

  out.push(labelLine(labels.structure));
  for (const step of pauta.structure || []) {
    out.push(labeledBullet(null, step));
  }

  if (pauta.sources && pauta.sources.length) {
    out.push(labelLine(labels.sources));
    for (const source of pauta.sources) {
      out.push(sourceBullet(source));
    }
  }

  out.push(labelLine(labels.keywords));
  out.push(body(pauta.keywords));

  out.push(labelLine(labels.tone));
  out.push(body(pauta.tone));

  return out;
}

function renderMonth(month) {
  const out = [];
  out.push(heading(month.label, 1));
  out.push(heading(month.axis_title, 3));
  if (month.axis_description) {
    out.push(body(month.axis_description));
  }
  for (const pauta of month.pautas || []) {
    out.push(...renderPauta(pauta));
  }
  return out;
}

const children = [];

children.push(
  new Paragraph({
    heading: HeadingLevel.TITLE,
    children: [new TextRun({ text: plan.title })],
  })
);
if (plan.subtitle) {
  children.push(
    new Paragraph({
      alignment: AlignmentType.CENTER,
      children: [new TextRun({ text: plan.subtitle, italics: true })],
    })
  );
}
if (plan.channel) {
  children.push(
    new Paragraph({
      alignment: AlignmentType.CENTER,
      children: [new TextRun({ text: plan.channel, italics: true, color: "595959" })],
    })
  );
}

children.push(...renderFreeformSections(plan.sections_before_months));

for (const month of plan.months || []) {
  children.push(...renderMonth(month));
}

children.push(...renderFreeformSections(plan.closing_sections));

const doc = new Document({
  numbering: {
    config: [
      {
        reference: BULLET_REF,
        levels: [
          {
            level: 0,
            format: LevelFormat.BULLET,
            text: "•",
            alignment: AlignmentType.LEFT,
            style: {
              paragraph: {
                indent: { left: 720, hanging: 360 },
              },
            },
          },
        ],
      },
    ],
  },
  sections: [
    {
      properties: {},
      children,
    },
  ],
});

Packer.toBuffer(doc).then((buffer) => {
  fs.mkdirSync(path.dirname(outputPath), { recursive: true });
  fs.writeFileSync(outputPath, buffer);
  console.log(`Wrote ${outputPath}`);
});
