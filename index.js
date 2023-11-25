const express = require("express");
const cors = require("cors");
const data = require("./database.json");

const app = express();
app.use(cors());

const port = process.env.PORT || 5000;

app.get("/api/viagens", (req, res) => {
  res.json(data.viagens);
});

app.listen(port, () => {
  console.log(`Servidor rodando na porta ${port}`);
});
