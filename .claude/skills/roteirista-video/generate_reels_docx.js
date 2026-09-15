const { Document, Packer, Paragraph, TextRun, HeadingLevel } = require('docx');
const fs = require('fs');
const path = require('path');

const reelsPath = process.argv[2] || './reels.json';
const outputPath = process.argv[3] || './reels-output.docx';

const reels = JSON.parse(fs.readFileSync(reelsPath, 'utf8'));

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
    spacing: { line: 300, after: 80 }
  });
};

const sections = [];

// Title
sections.push(
  createHeading(reels.title, 0),
  createNormal(reels.subtitle),
  createNormal(`Canal: ${reels.channel}`),
  new Paragraph({ text: '', spacing: { after: 200 } })
);

// Intro
sections.push(createHeading(reels.intro.heading, 1));
sections.push(createNormal(reels.intro.text));
sections.push(createNormal(reels.intro.structure, true));
sections.push(new Paragraph({ text: '', spacing: { after: 200 } }));

// Process each month
reels.reels.forEach(month => {
  sections.push(createHeading(month.month, 1));
  sections.push(createHeading(month.theme, 2));
  sections.push(new Paragraph({ text: '', spacing: { after: 150 } }));

  month.reels.forEach(reel => {
    sections.push(createHeading(`${reel.number}. ${reel.headline}`, 3));

    sections.push(createNormal(`Tópico: ${reel.topic}`, true));
    sections.push(createNormal(`Ângulo: ${reel.angle}`));
    sections.push(createNormal(`Duração: ${reel.duration} | Formato: ${reel.format}`));
    sections.push(new Paragraph({ text: '', spacing: { after: 100 } }));

    sections.push(createNormal('Conceito Visual:', true));
    sections.push(createNormal(reel.visual_concept));
    sections.push(new Paragraph({ text: '', spacing: { after: 100 } }));

    sections.push(createNormal('Copy:', true));
    sections.push(createNormal(reel.copy));
    sections.push(new Paragraph({ text: '', spacing: { after: 100 } }));

    sections.push(createNormal('CTA:', true));
    sections.push(createNormal(reel.cta));
    sections.push(new Paragraph({ text: '', spacing: { after: 100 } }));

    sections.push(createNormal('Keywords:', true));
    sections.push(createNormal(reel.keywords.join(', ')));
    sections.push(new Paragraph({ text: '', spacing: { after: 200 } }));
  });
});

// Closing
sections.push(new Paragraph({ text: '', spacing: { after: 200 } }));
sections.push(createHeading(reels.closing.heading, 1));
reels.closing.bullet_points.forEach(point => sections.push(createBullet(point)));

const doc = new Document({
  sections: [{
    children: sections
  }]
});

Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync(outputPath, buffer);
  console.log(`Wrote ${outputPath}`);
});
