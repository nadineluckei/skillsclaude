const { Document, Packer, Paragraph, TextRun, HeadingLevel } = require('docx');
const fs = require('fs');
const path = require('path');

const mdPath = process.argv[2] || './input.md';
const outputPath = process.argv[3] || './output.docx';

const content = fs.readFileSync(mdPath, 'utf8');
const lines = content.split('\n');

const sections = [];

lines.forEach((line, index) => {
  if (line.startsWith('# ')) {
    sections.push(new Paragraph({
      text: line.replace('# ', ''),
      heading: HeadingLevel.HEADING_1,
      spacing: { before: 400, after: 200 }
    }));
  } else if (line.startsWith('## ')) {
    sections.push(new Paragraph({
      text: line.replace('## ', ''),
      heading: HeadingLevel.HEADING_2,
      spacing: { before: 300, after: 150 }
    }));
  } else if (line.startsWith('### ')) {
    sections.push(new Paragraph({
      text: line.replace('### ', ''),
      heading: HeadingLevel.HEADING_3,
      spacing: { before: 250, after: 100 }
    }));
  } else if (line.startsWith('#### ')) {
    sections.push(new Paragraph({
      text: line.replace('#### ', ''),
      heading: HeadingLevel.HEADING_4,
      spacing: { before: 200, after: 80 }
    }));
  } else if (line.startsWith('**') && line.endsWith('**')) {
    sections.push(new Paragraph({
      text: new TextRun({
        text: line.replace(/\*\*/g, ''),
        bold: true
      }),
      spacing: { line: 300, after: 80 }
    }));
  } else if (line.trim() === '') {
    sections.push(new Paragraph({
      text: '',
      spacing: { after: 150 }
    }));
  } else if (line.trim()) {
    sections.push(new Paragraph({
      text: line,
      spacing: { line: 300, after: 100 }
    }));
  }
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
