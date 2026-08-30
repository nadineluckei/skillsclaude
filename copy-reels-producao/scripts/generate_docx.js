const fs = require('fs');
const path = require('path');
const { Document, Packer, Paragraph, Heading, TextRun, Table, TableRow, TableCell, WidthType, BorderStyle, AlignmentType, VerticalAlign } = require('docx');

function generateDocx(inputPath, outputPath) {
  // Read JSON
  const rawData = fs.readFileSync(inputPath, 'utf-8');
  const data = JSON.parse(rawData);

  // Metadata
  const title = `ROTEIRO PRODUÇÃO: ${data.metadata.titulo}`;
  const metadata = data.metadata || {};
  const producaoTable = data.producaoTable || [];
  const assets = data.assetsNecessarios || {};
  const qualityChecks = data.qualityChecklist || {};
  const notasEdicao = data.notasEdicao || '';

  const sections = [];

  // Title
  sections.push(
    new Paragraph({
      text: title,
      heading: 'Heading1',
      spacing: { after: 200 }
    })
  );

  // Metadata section
  sections.push(
    new Paragraph({
      text: 'METADATA',
      heading: 'Heading2',
      spacing: { after: 100 }
    })
  );

  const metadataTable = new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    rows: [
      new TableRow({
        cells: [
          new TableCell({ children: [new Paragraph('Título')] }),
          new TableCell({ children: [new Paragraph(metadata.titulo || '—')] })
        ]
      }),
      new TableRow({
        cells: [
          new TableCell({ children: [new Paragraph('Tipo')] }),
          new TableCell({ children: [new Paragraph(metadata.tipo || '—')] })
        ]
      }),
      new TableRow({
        cells: [
          new TableCell({ children: [new Paragraph('Duração')] }),
          new TableCell({ children: [new Paragraph(metadata.duracao || '—')] })
        ]
      }),
      new TableRow({
        cells: [
          new TableCell({ children: [new Paragraph('Nível de Produção')] }),
          new TableCell({ children: [new Paragraph(metadata.nivelProducao || '—')] })
        ]
      })
    ]
  });

  sections.push(metadataTable);
  sections.push(new Paragraph({ text: '', spacing: { after: 200 } }));

  // Produção Table
  sections.push(
    new Paragraph({
      text: 'TABELA DE PRODUÇÃO',
      heading: 'Heading2',
      spacing: { after: 100 }
    })
  );

  const prodRows = [];

  // Header row
  prodRows.push(
    new TableRow({
      cells: [
        new TableCell({
          children: [new Paragraph({ text: 'Timing', bold: true })],
          width: { size: 10, type: WidthType.PERCENTAGE },
          shading: { fill: 'CCCCCC' }
        }),
        new TableCell({
          children: [new Paragraph({ text: 'Visual', bold: true })],
          width: { size: 25, type: WidthType.PERCENTAGE },
          shading: { fill: 'CCCCCC' }
        }),
        new TableCell({
          children: [new Paragraph({ text: 'Voiceover', bold: true })],
          width: { size: 20, type: WidthType.PERCENTAGE },
          shading: { fill: 'CCCCCC' }
        }),
        new TableCell({
          children: [new Paragraph({ text: 'On-Screen Text', bold: true })],
          width: { size: 20, type: WidthType.PERCENTAGE },
          shading: { fill: 'CCCCCC' }
        }),
        new TableCell({
          children: [new Paragraph({ text: 'Transição/Efeito', bold: true })],
          width: { size: 25, type: WidthType.PERCENTAGE },
          shading: { fill: 'CCCCCC' }
        })
      ]
    })
  );

  // Data rows
  producaoTable.forEach(row => {
    prodRows.push(
      new TableRow({
        cells: [
          new TableCell({
            children: [new Paragraph(row.timeRange || '—')],
            verticalAlign: VerticalAlign.TOP
          }),
          new TableCell({
            children: [new Paragraph(row.visual || '—')],
            verticalAlign: VerticalAlign.TOP
          }),
          new TableCell({
            children: [new Paragraph(row.voiceover || '—')],
            verticalAlign: VerticalAlign.TOP
          }),
          new TableCell({
            children: [new Paragraph((row.onScreenText || '—').replace(/\n/g, '\n'))],
            verticalAlign: VerticalAlign.TOP
          }),
          new TableCell({
            children: [new Paragraph(row.transicao || '—')],
            verticalAlign: VerticalAlign.TOP
          })
        ]
      })
    );
  });

  const prodTableObj = new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    rows: prodRows
  });

  sections.push(prodTableObj);
  sections.push(new Paragraph({ text: '', spacing: { after: 200 } }));

  // Assets Necessarios
  if (Object.keys(assets).length > 0) {
    sections.push(
      new Paragraph({
        text: 'ASSETS NECESSÁRIOS',
        heading: 'Heading2',
        spacing: { after: 100 }
      })
    );

    if (assets.video && assets.video.length > 0) {
      sections.push(new Paragraph({ text: '📹 Vídeo', bold: true, spacing: { after: 50 } }));
      assets.video.forEach(v => {
        sections.push(new Paragraph({
          text: `• ${v}`,
          spacing: { after: 25 }
        }));
      });
      sections.push(new Paragraph({ text: '', spacing: { after: 100 } }));
    }

    if (assets.audio && assets.audio.length > 0) {
      sections.push(new Paragraph({ text: '🎵 Áudio', bold: true, spacing: { after: 50 } }));
      assets.audio.forEach(a => {
        sections.push(new Paragraph({
          text: `• ${a}`,
          spacing: { after: 25 }
        }));
      });
      sections.push(new Paragraph({ text: '', spacing: { after: 100 } }));
    }

    if (assets.texto && assets.texto.length > 0) {
      sections.push(new Paragraph({ text: '✍️ Texto/Tipografia', bold: true, spacing: { after: 50 } }));
      assets.texto.forEach(t => {
        sections.push(new Paragraph({
          text: `• ${t}`,
          spacing: { after: 25 }
        }));
      });
      sections.push(new Paragraph({ text: '', spacing: { after: 100 } }));
    }

    if (assets.outros && assets.outros.length > 0) {
      sections.push(new Paragraph({ text: '⚙️ Outros', bold: true, spacing: { after: 50 } }));
      assets.outros.forEach(o => {
        sections.push(new Paragraph({
          text: `• ${o}`,
          spacing: { after: 25 }
        }));
      });
      sections.push(new Paragraph({ text: '', spacing: { after: 200 } }));
    }
  }

  // Quality Checklist
  if (Object.keys(qualityChecks).length > 0) {
    sections.push(
      new Paragraph({
        text: 'QUALITY CHECKLIST',
        heading: 'Heading2',
        spacing: { after: 100 }
      })
    );

    Object.entries(qualityChecks).forEach(([key, value]) => {
      const emoji = value ? '✅' : '❌';
      const label = key
        .replace(/([A-Z])/g, ' $1')
        .replace(/^./, str => str.toUpperCase())
        .trim();

      sections.push(new Paragraph({
        text: `${emoji} ${label}`,
        spacing: { after: 50 }
      }));
    });

    sections.push(new Paragraph({ text: '', spacing: { after: 200 } }));
  }

  // Notas de Edição
  if (notasEdicao) {
    sections.push(
      new Paragraph({
        text: 'NOTAS DE EDIÇÃO & BRAND',
        heading: 'Heading2',
        spacing: { after: 100 }
      })
    );

    sections.push(new Paragraph({
      text: notasEdicao,
      spacing: { after: 200 }
    }));
  }

  // Footer
  sections.push(new Paragraph({
    text: `Gerado em ${data.date || new Date().toISOString().split('T')[0]} | Copy-Reels Producao Skill`,
    size: 18,
    italics: true,
    alignment: AlignmentType.CENTER
  }));

  // Create document
  const doc = new Document({ sections: [{ children: sections }] });

  // Write to file
  Packer.toBuffer(doc).then(buffer => {
    fs.writeFileSync(outputPath, buffer);
    console.log(`✅ Documento de produção gerado: ${outputPath}`);
  });
}

// CLI usage
const args = process.argv.slice(2);
if (args.length < 2) {
  console.error('Usage: node generate_docx.js <input.json> <output.docx>');
  process.exit(1);
}

generateDocx(args[0], args[1]);
