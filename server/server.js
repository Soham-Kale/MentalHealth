require('dotenv').config();
const express = require("express");
const app = express();
const cors = require("cors"); 
const router = require("./router/auth-router");
const connectDB = require("./utils/db")

var corsOptions = {
    origin:  ["https://mindguardai.vercel.app","http://localhost:5173/login"],
    method: "GET, POST, PUT, PATCH, HEAD",
    credential: true
}

app.use(cors(corsOptions));
app.use(express.json());

app.use("/api/auth", router);

const PORT = 8000;
connectDB().then(() => {
    app.listen(PORT, () => {
        console.log(`server running at port ${PORT}`);
    })
})