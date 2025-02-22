const express = require("express");
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware (optional)
app.use(express.json());

// Sample Route
app.get("/", (req, res) => {
    res.send("🚀 Server is running successfully!");
});

// Start Server
app.listen(PORT, () => {
    console.log(`✅ Server is running on port ${PORT}`);
});
