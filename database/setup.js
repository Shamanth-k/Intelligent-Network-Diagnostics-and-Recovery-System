// Run with: node setup.js
// This initializes the database with an index on timestamp (optional)
const { MongoClient } = require('mongodb');
const uri = "mongodb://localhost:27017/";
const client = new MongoClient(uri, { useUnifiedTopology: true });

async function main() {
  try {
    await client.connect();
    const db = client.db("intellinet");
    const col = db.collection("network_logs");
    // create index on timestamp (string ISO format) - optional
    await col.createIndex({ "timestamp": -1 });
    console.log("Database initialized.");
  } catch (err) {
    console.error(err);
  } finally {
    await client.close();
  }
}

main();
