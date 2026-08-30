#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const { Document, Packer, Paragraph, TextRun, HeadingLevel, BorderStyle, convertInchesToTwip } = require('docx');

const inputFile = process.argv[2];
const outputFile = process.argv[3] || 'output.docx';

if (!inputFile) {
  console.error('Usage: node generate_docx.js <input.json> [output.docx]');
  process.exit(1);
}

const data = JSON.parse(fs.readFileSync(inputFile, 'utf8'));

const sections = [];

// Title
sections.push(
  new Paragraph({
    text: 'PESQUISA DE TEMAS',
    heading: HeadingLevel.HEADING_1,
    spacing: { after: 100 }
  }),
  new Paragraph({
    text: `Data: ${data.date || new Date().toLocaleDateString('pt-BR')}`,
    spacing: { after: 400 }
  })
);

// Temas Rápidos
if (data.rapidThemes && data.rapidThemes.length > 0) {
  sections.push(
    new Paragraph({
      text: 'TEMAS RÁPIDOS',
      heading: HeadingLevel.HEADING_2,
      spacing: { before: 200, after: 200 }
    })
  );

  data.rapidThemes.forEach((theme, idx) => {
    sections.push(
      new Paragraph({
        text: theme.title,
        heading: HeadingLevel.HEADING_3,
        spacing: { before: 150, after: 100 }
      }),
      new Paragraph({
        text: 'Por que tá em alta: ',
        bold: true,
        spacing: { after: 50 }
      }),
      new Paragraph({
        text: theme.why,
        spacing: { after: 100 }
      }),
      new Paragraph({
        text: 'Ângulo para social: ',
        bold: true,
        spacing: { after: 50 }
      }),
      new Paragraph({
        text: `"${theme.socialAngle}"`,
        spacing: { after: 100 },
        italics: true
      }),
      new Paragraph({
        text: `Fonte: ${theme.source}`,
        spacing: { after: 300 },
        italics: true,
        size: 20
      })
    );
  });

  sections.push(
    new Paragraph({
      text: '',
      spacing: { after: 200 }
    })
  );
}

// Temas Robustos
if ((data.painPoints && data.painPoints.length > 0) || (data.risingThemes && data.risingThemes.length > 0)) {
  sections.push(
    new Paragraph({
      text: 'TEMAS ROBUSTOS',
      heading: HeadingLevel.HEADING_2,
      spacing: { before: 200, after: 200 }
    })
  );

  // Dores Específicas
  if (data.painPoints && data.painPoints.length > 0) {
    sections.push(
      new Paragraph({
        text: 'Editoria: Dores Específicas',
        heading: HeadingLevel.HEADING_3,
        spacing: { before: 150, after: 150 }
      })
    );

    data.painPoints.forEach((pain) => {
      sections.push(
        new Paragraph({
          text: pain.pain,
          heading: HeadingLevel.HEADING_4,
          spacing: { before: 100, after: 80 }
        }),
        new Paragraph({
          text: 'Dado/Citação: ',
          bold: true,
          spacing: { after: 50 }
        }),
        new Paragraph({
          text: `"${pain.data}"`,
          spacing: { after: 100 },
          italics: true
        }),
        new Paragraph({
          text: 'Por que é dor agora: ',
          bold: true,
          spacing: { after: 50 }
        }),
        new Paragraph({
          text: pain.why,
          spacing: { after: 100 }
        }),
        new Paragraph({
          text: 'Quem sofre: ',
          bold: true,
          spacing: { after: 50 }
        }),
        new Paragraph({
          text: pain.whoAffected,
          spacing: { after: 100 }
        }),
        new Paragraph({
          text: `Fonte: ${pain.source}`,
          spacing: { after: 250 },
          italics: true,
          size: 20
        })
      );
    });

    sections.push(
      new Paragraph({
        text: '',
        spacing: { after: 200 }
      })
    );
  }

  // Temas em Alta
  if (data.risingThemes && data.risingThemes.length > 0) {
    sections.push(
      new Paragraph({
        text: 'Editoria: Temas em Alta',
        heading: HeadingLevel.HEADING_3,
        spacing: { before: 150, after: 150 }
      })
    );

    data.risingThemes.forEach((theme) => {
      sections.push(
        new Paragraph({
          text: theme.theme,
          heading: HeadingLevel.HEADING_4,
          spacing: { before: 100, after: 80 }
        }),
        new Paragraph({
          text: 'O que é: ',
          bold: true,
          spacing: { after: 50 }
        }),
        new Paragraph({
          text: theme.definition,
          spacing: { after: 100 }
        }),
        new Paragraph({
          text: 'Por que tá em alta: ',
          bold: true,
          spacing: { after: 50 }
        }),
        new Paragraph({
          text: theme.why,
          spacing: { after: 100 }
        }),
        new Paragraph({
          text: 'Onde tá em alta: ',
          bold: true,
          spacing: { after: 50 }
        }),
        new Paragraph({
          text: theme.whereHot,
          spacing: { after: 100 }
        }),
        new Paragraph({
          text: 'Próximos 6 meses: ',
          bold: true,
          spacing: { after: 50 }
        }),
        new Paragraph({
          text: theme.next6Months,
          spacing: { after: 100 }
        }),
        new Paragraph({
          text: `Fonte: ${theme.source}`,
          spacing: { after: 250 },
          italics: true,
          size: 20
        })
      );
    });

    sections.push(
      new Paragraph({
        text: '',
        spacing: { after: 200 }
      })
    );
  }
}

// Executive Summary
if (data.executiveSummary) {
  sections.push(
    new Paragraph({
      text: 'RESUMO EXECUTIVO',
      heading: HeadingLevel.HEADING_2,
      spacing: { before: 300, after: 150 }
    }),
    new Paragraph({
      text: data.executiveSummary,
      spacing: { after: 200 }
    })
  );
}

const doc = new Document({
  sections: [
    {
      children: sections
    }
  ]
});

Packer.toBuffer(doc).then((buffer) => {
  fs.writeFileSync(outputFile, buffer);
  console.log(`✓ Documento gerado: ${outputFile}`);
});
