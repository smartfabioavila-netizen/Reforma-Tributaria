// Uso: node pdf.cjs entrada.html saida.pdf [paisagem]
// Requer o pacote "playwright" (local ou global, via NODE_PATH).
const { chromium } = require("playwright");
const { pathToFileURL } = require("node:url");
const path = require("node:path");

(async () => {
  const [entrada, saida, orientacao] = process.argv.slice(2);
  const opcoes = process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {};
  const browser = await chromium.launch(opcoes);
  const page = await browser.newPage();
  await page.goto(pathToFileURL(path.resolve(entrada)).href, { waitUntil: "networkidle" });
  const paisagem = orientacao === "paisagem";
  await page.pdf({
    path: saida,
    format: "A4",
    landscape: paisagem,
    printBackground: true,
    preferCSSPageSize: true,
    displayHeaderFooter: !paisagem,
    headerTemplate: "<span></span>",
    footerTemplate: `<div style="width:100%;font-family:Inter,sans-serif;font-size:7.5pt;color:#8a94a3;padding:0 16mm;display:flex;justify-content:space-between">
      <span>KIT · Claude para Reforma Tributária 2026</span><span class="pageNumber"></span></div>`,
  });
  await browser.close();
})();
