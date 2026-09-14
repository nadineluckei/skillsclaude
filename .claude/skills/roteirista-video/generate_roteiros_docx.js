const { Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableCell, TableRow, AlignmentType } = require('docx');
const fs = require('fs');
const path = require('path');

const roteirosPath = process.argv[2] || './roteiros.json';
const outputPath = process.argv[3] || './roteiros-output.docx';

const roteiros = JSON.parse(fs.readFileSync(roteirosPath, 'utf8'));

const createHeading = (text, level = 1) => {
  return new Paragraph({
    text,
    heading: HeadingLevel[`HEADING_${level}`],
    spacing: { before: 200, after: 100 }
  });
};

const createBullet = (text) => {
  return new Paragraph({
    text,
    bullet: { level: 0 },
    spacing: { line: 300 }
  });
};

const createNormal = (text, bold = false) => {
  return new Paragraph({
    text: new TextRun({
      text,
      bold
    }),
    spacing: { line: 300, after: 100 }
  });
};

const sections = [];

// Title
sections.push(
  createHeading(roteiros.title, 0),
  createNormal(roteiros.subtitle),
  createNormal(`Canal: ${roteiros.channel}`),
  new Paragraph({ text: '', spacing: { after: 200 } })
);

// Intro sections
roteiros.intro_sections.forEach(section => {
  sections.push(createHeading(section.heading, section.level));
  section.paragraphs.forEach(p => sections.push(createNormal(p)));
  sections.push(new Paragraph({ text: '', spacing: { after: 100 } }));
});

// Process each month
roteiros.roteiros.forEach(month => {
  sections.push(new Paragraph({ text: '', spacing: { after: 200 } }));
  sections.push(createHeading(month.month, 1));
  sections.push(createHeading(month.month_title, 2));

  month.scripts.forEach(script => {
    sections.push(new Paragraph({ text: '', spacing: { after: 150 } }));
    sections.push(createHeading(`Roteiro ${script.number}: ${script.title}`, 2));

    sections.push(createNormal(`Duração: ${script.duration}`, true));
    sections.push(createNormal(`Tom: ${script.tone}`, true));
    sections.push(new Paragraph({ text: '', spacing: { after: 150 } }));

    // Script sections
    sections.push(createHeading('SCRIPT', 3));

    Object.entries(script.script).forEach(([key, section]) => {
      const sectionTitle = key
        .split('_')
        .map(word => word.charAt(0).toUpperCase() + word.slice(1))
        .join(' ');

      sections.push(createHeading(sectionTitle, 4));
      sections.push(createNormal(`[${section.duration}]`, true));
      sections.push(createNormal(section.text));
      sections.push(new Paragraph({ text: '', spacing: { after: 100 } }));
    });

    // Reels
    sections.push(new Paragraph({ text: '', spacing: { after: 150 } }));
    sections.push(createHeading('CORTES PARA REELS', 3));

    script.reels.forEach(reel => {
      sections.push(createHeading(`Reel ${reel.number}: ${reel.title}`, 4));
      sections.push(createBullet(`Timestamp: ${reel.timestamp}`));
      sections.push(createBullet(`Headline: ${reel.headline}`));
      sections.push(createBullet(`Conceito: ${reel.concept}`));
      sections.push(new Paragraph({ text: '', spacing: { after: 100 } }));
    });

    sections.push(new Paragraph({ text: '', spacing: { after: 200 } }));
  });
});

const doc = new Document({
  sections: [{
    children: sections
  }]
});

Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync(outputPath, buffer);
  console.log(`Wrote ${outputPath}`);
});
