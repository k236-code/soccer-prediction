const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");
require("dotenv").config();

const app = express();
app.use(express.json());
app.use(cors());

mongoose.connect(process.env.MONGO_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

const TeamSchema = new mongoose.Schema({
  name: String,
  stats: Object,
});

const Team = mongoose.model("Team", TeamSchema);

app.get("/teams", async (req, res) => {
  const teams = await Team.find();
  res.json(teams);
});

app.post("/compare", async (req, res) => {
  const { team1, team2 } = req.body;
  const teamA = await Team.findById(team1);
  const teamB = await Team.findById(team2);

  res.json({
    teamA: teamA.name,
    teamB: teamB.name,
    comparison: {
      goals: teamA.stats.goals - teamB.stats.goals,
      wins: teamA.stats.wins - teamB.stats.wins,
    },
  });
});

app.listen(5000, () => console.log("Server running on port 5000"));
