#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const { Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType, BorderStyle, Table, TableCell, TableRow, VerticalAlign, convertInchesToTwip, PageBreak, UnorderedList, OrderedList } = require('docx');

function parseMarkdown(content) {
  const lines = content.split('\n');
  const elements = [];
  let i = 0;

  while (i < lines.length) {
    const line = lines[i];

    // Skip empty lines
    if (!line.trim()) {
      i++;
      continue;
    }

    // Headings
    if (line.startsWith('# ')) {
      elements.push({
        type: 'heading1',
        text: line.replace(/^# /, '').trim()
      });
      i++;
      continue;
    }

    if (line.startsWith('## ')) {
      elements.push({
        type: 'heading2',
        text: line.replace(/^## /, '').trim()
      });
      i++;
      continue;
    }

    if (line.startsWith('### ')) {
      elements.push({
        type: 'heading3',
        text: line.replace(/^### /, '').trim()
      });
      i++;
      continue;
    }

    if (line.startsWith('#### ')) {
      elements.push({
        type: 'heading4',
        text: line.replace(/^#### /, '').trim()
      });
      i++;
      continue;
    }

    // Lists
    if (line.trim().startsWith('- ')) {
      const listItems = [];
      while (i < lines.length && (lines[i].trim().startsWith('- ') || lines[i].trim().startsWith('* ') || lines[i].startsWith('  '))) {
        if (lines[i].trim().startsWith('- ') || lines[i].trim().startsWith('* ')) {
          listItems.push(lines[i].replace(/^[-*]\s/, '').trim());
        }
        i++;
      }
      elements.push({
        type: 'list',
        items: listItems,
        ordered: false
      });
      continue;
    }

    if (line.trim().match(/^\d+\.\s/)) {
      const listItems = [];
      while (i < lines.length && lines[i].trim().match(/^\d+\.\s/)) {
        listItems.push(lines[i].replace(/^\d+\.\s/, '').trim());
        i++;
      }
      elements.push({
        type: 'list',
        items: listItems,
        ordered: true
      });
      continue;
    }

    // Code blocks
    if (line.trim().startsWith('```')) {
      const codeLines = [];
      i++;
      while (i < lines.length && !lines[i].trim().startsWith('```')) {
        codeLines.push(lines[i]);
        i++;
      }
      i++; // Skip closing ```
      elements.push({
        type: 'code',
        text: codeLines.join('\n').trim()
      });
      continue;
    }

    // Horizontal rule
    if (line.trim() === '---') {
      elements.push({
        type: 'rule'
      });
      i++;
      continue;
    }

    // Regular paragraphs
    elements.push({
      type: 'paragraph',
      text: line.trim()
    });
    i++;
  }

  return elements;
}

function textToDocx(text) {
  // Parse inline formatting: **bold**, *italic*, [link](url)
  const runs = [];
  let currentText = '';
  let i = 0;

  while (i < text.length) {
    if (text.substr(i, 2) === '**') {
      if (currentText) runs.push(new TextRun(currentText));
      currentText = '';
      i += 2;
      let boldText = '';
      while (i < text.length && text.substr(i, 2) !== '**') {
        boldText += text[i];
        i++;
      }
      if (text.substr(i, 2) === '**') {
        runs.push(new TextRun({ text: boldText, bold: true }));
        i += 2;
      }
    } else if (text[i] === '*' && text[i - 1] !== '*') {
      if (currentText) runs.push(new TextRun(currentText));
      currentText = '';
      i++;
      let italicText = '';
      while (i < text.length && text[i] !== '*') {
        italicText += text[i];
        i++;
      }
      if (text[i] === '*') {
        runs.push(new TextRun({ text: italicText, italics: true }));
        i++;
      }
    } else {
      currentText += text[i];
      i++;
    }
  }

  if (currentText) runs.push(new TextRun(currentText));
  return runs.length > 0 ? runs : [new TextRun(text)];
}

function buildDocx(elements) {
  const sections = [];

  elements.forEach((el, idx) => {
    switch (el.type) {
      case 'heading1':
        sections.push(
          new Paragraph({
            text: el.text,
            heading: HeadingLevel.HEADING_1,
            spacing: { before: 240, after: 120 }
          })
        );
        break;

      case 'heading2':
        sections.push(
          new Paragraph({
            text: el.text,
            heading: HeadingLevel.HEADING_2,
            spacing: { before: 200, after: 100 }
          })
        );
        break;

      case 'heading3':
        sections.push(
          new Paragraph({
            text: el.text,
            heading: HeadingLevel.HEADING_3,
            spacing: { before: 160, after: 80 }
          })
        );
        break;

      case 'heading4':
        sections.push(
          new Paragraph({
            text: el.text,
            heading: HeadingLevel.HEADING_4,
            spacing: { before: 120, after: 60 }
          })
        );
        break;

      case 'paragraph':
        sections.push(
          new Paragraph({
            children: textToDocx(el.text),
            spacing: { after: 100 }
          })
        );
        break;

      case 'list':
        el.items.forEach((item, idx) => {
          sections.push(
            new Paragraph({
              text: item,
              bullet: { level: 0 },
              spacing: { after: 60 }
            })
          );
        });
        break;

      case 'code':
        sections.push(
          new Paragraph({
            children: [new TextRun({ text: el.text, font: 'Courier New', size: 20 })],
            shading: { fill: 'f0f0f0' },
            spacing: { before: 100, after: 100 }
          })
        );
        break;

      case 'rule':
        sections.push(
          new Paragraph({
            border: {
              bottom: {
                color: '000000',
                space: 1,
                style: BorderStyle.SINGLE,
                size: 6
              }
            },
            spacing: { before: 100, after: 100 }
          })
        );
        break;
    }
  });

  return new Document({
    sections: [
      {
        children: sections
      }
    ]
  });
}

async function main() {
  const args = process.argv.slice(2);
  const fileName = args[0] || 'blog-strategy';

  const markdownPath = `/tmp/claude-0/-home-user-skillsclaude/56a33cb1-8a8f-5cae-800d-56039414b217/scratchpad/${fileName}.md`;
  const outputPath = `/tmp/claude-0/-home-user-skillsclaude/56a33cb1-8a8f-5cae-800d-56039414b217/scratchpad/${fileName}.docx`;

  try {
    console.log('📄 Lendo markdown...');
    const markdown = fs.readFileSync(markdownPath, 'utf-8');

    console.log('🔄 Convertendo para DOCX...');
    const elements = parseMarkdown(markdown);
    const doc = buildDocx(elements);

    console.log('💾 Salvando DOCX...');
    const buffer = await Packer.toBuffer(doc);
    fs.writeFileSync(outputPath, buffer);

    console.log(`✅ DOCX criado com sucesso!`);
    console.log(`📍 Localização: ${outputPath}`);
  } catch (error) {
    console.error('❌ Erro:', error.message);
    process.exit(1);
  }
}

main();
