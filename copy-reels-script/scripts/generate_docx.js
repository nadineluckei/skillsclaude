const fs = require('fs');
const path = require('path');
const { Document, Packer, Paragraph, Heading, TextRun, Table, TableRow, TableCell, WidthType, BorderStyle, AlignmentType } = require('docx');

function generateDocx(inputPath, outputPath) {
  // Read JSON
  const rawData = fs.readFileSync(inputPath, 'utf-8');
  const data = JSON.parse(rawData);

  // Metadata
  const title = `ROTEIRO COPY-REELS: ${data.roteiroPrincipal.titulo}`;
  const metadata = data.metadata || {};
  const roteiro = data.roteiroPrincipal || {};
  const variations = data.hookVariations || [];
  const ctaVariants = data.ctaVariants || [];
  const testing = data.testingNotes || {};
  const qualityChecks = data.qualityChecks || {};

  const sections = [];

  // Title
  sections.push(
    new Paragraph({
      text: title,
      heading: 'Heading1',
      thematicBreak: false,
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
          new TableCell({ children: [new Paragraph('Objetivo')] }),
          new TableCell({ children: [new Paragraph(metadata.objetivo || '—')] })
        ]
      }),
      new TableRow({
        cells: [
          new TableCell({ children: [new Paragraph('Público')] }),
          new TableCell({ children: [new Paragraph(metadata.publico || '—')] })
        ]
      }),
      new TableRow({
        cells: [
          new TableCell({ children: [new Paragraph('Plataforma')] }),
          new TableCell({ children: [new Paragraph(metadata.plataforma || '—')] })
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
          new TableCell({ children: [new Paragraph('Tom')] }),
          new TableCell({ children: [new Paragraph(metadata.tom || '—')] })
        ]
      })
    ]
  });

  sections.push(metadataTable);
  sections.push(new Paragraph({ text: '', spacing: { after: 200 } }));

  // Roteiro Principal
  sections.push(
    new Paragraph({
      text: 'ROTEIRO PRINCIPAL',
      heading: 'Heading2',
      spacing: { after: 100 }
    })
  );

  // Hook
  sections.push(new Paragraph({ text: '🎬 HOOK (0–3s)', bold: true, spacing: { after: 50 } }));
  sections.push(new Paragraph({
    text: roteiro.hook?.texto || '—',
    italics: true,
    spacing: { after: 50 }
  }));
  sections.push(new Paragraph({
    text: `Padrão: ${roteiro.hook?.padrao || '—'} | Confiança: ${roteiro.hook?.confianca || '—'}`,
    size: 20,
    spacing: { after: 150 }
  }));

  // Setup
  sections.push(new Paragraph({ text: '⚙️ SETUP (3–8s)', bold: true, spacing: { after: 50 } }));
  sections.push(new Paragraph({
    text: roteiro.setup?.texto || '—',
    spacing: { after: 150 }
  }));

  // Solução
  sections.push(new Paragraph({ text: '💡 SOLUÇÃO (8–20s)', bold: true, spacing: { after: 50 } }));
  sections.push(new Paragraph({
    text: roteiro.solucao?.texto || '—',
    spacing: { after: 150 }
  }));

  // Benefit
  sections.push(new Paragraph({ text: '🎯 BENEFIT (20–27s)', bold: true, spacing: { after: 50 } }));
  sections.push(new Paragraph({
    text: roteiro.benefit?.texto || '—',
    spacing: { after: 150 }
  }));

  // CTA
  sections.push(new Paragraph({ text: '🔗 CTA (27–30s)', bold: true, spacing: { after: 50 } }));
  sections.push(new Paragraph({
    text: roteiro.cta?.texto || '—',
    italics: true,
    spacing: { after: 50 }
  }));
  sections.push(new Paragraph({
    text: `Tipo: ${roteiro.cta?.tipo || '—'}`,
    size: 20,
    spacing: { after: 200 }
  }));

  // Hook Variations
  if (variations.length > 0) {
    sections.push(
      new Paragraph({
        text: 'VARIAÇÕES DE HOOK (A/B TESTING)',
        heading: 'Heading2',
        spacing: { after: 100 }
      })
    );

    variations.forEach((v, idx) => {
      sections.push(new Paragraph({
        text: `Variação ${idx + 1}: ${v.padrao}`,
        bold: true,
        spacing: { after: 50 }
      }));
      sections.push(new Paragraph({
        text: v.texto,
        italics: true,
        spacing: { after: 100 }
      }));
    });

    sections.push(new Paragraph({ text: '', spacing: { after: 200 } }));
  }

  // CTA Variants
  if (ctaVariants.length > 0) {
    sections.push(
      new Paragraph({
        text: 'VARIAÇÕES DE CTA',
        heading: 'Heading2',
        spacing: { after: 100 }
      })
    );

    ctaVariants.forEach((c, idx) => {
      sections.push(new Paragraph({
        text: `${idx + 1}. ${c.texto}`,
        bold: true,
        spacing: { after: 50 }
      }));
      sections.push(new Paragraph({
        text: `Tipo: ${c.tipo} | ${c.notaDeUso || ''}`,
        size: 20,
        spacing: { after: 100 }
      }));
    });

    sections.push(new Paragraph({ text: '', spacing: { after: 200 } }));
  }

  // Testing Notes
  if (Object.keys(testing).length > 0) {
    sections.push(
      new Paragraph({
        text: 'TESTING NOTES',
        heading: 'Heading2',
        spacing: { after: 100 }
      })
    );

    const testingTable = new Table({
      width: { size: 100, type: WidthType.PERCENTAGE },
      rows: [
        new TableRow({
          cells: [
            new TableCell({ children: [new Paragraph('Métrica Principal')] }),
            new TableCell({ children: [new Paragraph(testing.metricaPrincipal || '—')] })
          ]
        }),
        new TableRow({
          cells: [
            new TableCell({ children: [new Paragraph('Duração')] }),
            new TableCell({ children: [new Paragraph(testing.duracao || '—')] })
          ]
        }),
        new TableRow({
          cells: [
            new TableCell({ children: [new Paragraph('Benchmark')] }),
            new TableCell({ children: [new Paragraph(testing.benchmark || '—')] })
          ]
        }),
        new TableRow({
          cells: [
            new TableCell({ children: [new Paragraph('Next Steps')] }),
            new TableCell({ children: [new Paragraph(testing.nextSteps || '—')] })
          ]
        })
      ]
    });

    sections.push(testingTable);
    sections.push(new Paragraph({ text: '', spacing: { after: 200 } }));
  }

  // Quality Checks
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

  // Notes (if available)
  if (data.notasBrand) {
    sections.push(
      new Paragraph({
        text: 'NOTAS DE BRAND ALIGNMENT',
        heading: 'Heading2',
        spacing: { after: 100 }
      })
    );

    sections.push(new Paragraph({
      text: data.notasBrand.alinhamentoComMarca || '—',
      spacing: { after: 100 }
    }));

    sections.push(new Paragraph({
      text: `Exemplo de aplicação: ${data.notasBrand.exemploBrand || '—'}`,
      italics: true,
      spacing: { after: 200 }
    }));
  }

  // Footer
  sections.push(new Paragraph({
    text: `Gerado em ${data.date || new Date().toISOString().split('T')[0]} | Copy-Reels Script Skill`,
    size: 18,
    italics: true,
    alignment: AlignmentType.CENTER
  }));

  // Create document
  const doc = new Document({ sections: [{ children: sections }] });

  // Write to file
  Packer.toBuffer(doc).then(buffer => {
    fs.writeFileSync(outputPath, buffer);
    console.log(`✅ Documento gerado: ${outputPath}`);
  });
}

// CLI usage
const args = process.argv.slice(2);
if (args.length < 2) {
  console.error('Usage: node generate_docx.js <input.json> <output.docx>');
  process.exit(1);
}

generateDocx(args[0], args[1]);
