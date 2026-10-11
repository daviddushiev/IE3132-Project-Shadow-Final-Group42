const express = require("express");
const session = require("express-session");
const { DatabaseSync } = require("node:sqlite");

const app = express();
const PORT = 3000;

app.use(express.urlencoded({ extended: false }));

app.use(
    session({
        secret: process.env.SESSION_SECRET || "project-shadow-development-secret",
        resave: false,
        saveUninitialized: false,
        cookie: {
            httpOnly: true,
            sameSite: "lax"
        }
    })
);

// ---------------------------------------------------------
// SQLite database
// ---------------------------------------------------------

const db = new DatabaseSync("/app/portal.db");

db.exec(`
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        display_name TEXT NOT NULL,
        role TEXT NOT NULL
    );

    DELETE FROM users;

    INSERT INTO users
        (id, username, password, display_name, role)
    VALUES
        (1, 'jalvarez', 'S0lace-Research-927!', 'J Alvarez', 'Senior Research Analyst');
`);

const FLAG =
    process.env.STAGE2_FLAG ||
    "SHADOW{sql_injection_opens_the_portal}";

function page(title, body) {
    return `
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, initial-scale=1.0">

    <title>${title} | Solace Dynamics</title>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #07111f;
            color: #e2e8f0;
        }

        header {
            background: #0f172a;
            padding: 22px 8%;
            border-bottom: 1px solid #334155;
        }

        header h1 {
            margin: 0;
            color: #38bdf8;
        }

        header p {
            color: #94a3b8;
        }

        main {
            max-width: 850px;
            margin: 50px auto;
            padding: 0 25px;
        }

        .card {
            background: #111c2f;
            padding: 30px;
            border-radius: 10px;
            margin-bottom: 25px;
        }

        label {
            display: block;
            margin-top: 18px;
            margin-bottom: 7px;
        }

        input {
            width: 100%;
            padding: 12px;
            border-radius: 5px;
            border: 1px solid #475569;
            background: #0f172a;
            color: white;
        }

        button {
            margin-top: 22px;
            padding: 12px 25px;
            background: #0284c7;
            color: white;
            border: 0;
            border-radius: 5px;
            cursor: pointer;
        }

        .error {
            background: #451a1a;
            border-left: 5px solid #ef4444;
            padding: 15px;
            margin-bottom: 20px;
        }

        .notice {
            background: #172554;
            border-left: 5px solid #3b82f6;
            padding: 18px;
            margin: 20px 0;
        }

        .flag {
            background: #052e16;
            border-left: 5px solid #22c55e;
            padding: 20px;
            margin: 25px 0;
            font-family: monospace;
            font-size: 18px;
        }

        code {
            background: #1e293b;
            padding: 3px 7px;
            border-radius: 4px;
        }

        a {
            color: #38bdf8;
        }
    </style>

</head>

<body>

<header>
    <h1>Solace Dynamics</h1>
    <p>Secure Research Portal</p>
</header>

<main>
    ${body}
</main>

</body>
</html>
`;
}

// ---------------------------------------------------------
// Login page
// ---------------------------------------------------------

app.get("/", (req, res) => {

    if (req.session.user) {
        return res.redirect("/dashboard");
    }

    res.send(
        page(
            "Research Portal",
            `
            <div class="card">

                <h2>Researcher Authentication</h2>

                <p>
                    This system is restricted to authorised
                    Solace Dynamics research personnel.
                </p>

                <form method="POST" action="/login">

                    <label>Username</label>
                    <input
                        type="text"
                        name="username"
                        autocomplete="off"
                        required
                    >

                    <label>Password</label>
                    <input
                        type="password"
                        name="password"
                        autocomplete="off"
                        required
                    >

                    <button type="submit">
                        Sign In
                    </button>

                </form>

            </div>
            `
        )
    );
});

// ---------------------------------------------------------
// Intentionally vulnerable authentication
// ---------------------------------------------------------

app.post("/login", (req, res) => {

    const username = req.body.username || "";
    const password = req.body.password || "";

    /*
     * INTENTIONALLY VULNERABLE FOR IE3132 CTF
     *
     * User-controlled values are concatenated directly into
     * the SQL statement instead of using parameterised queries.
     */

    const sql = `
        SELECT id, username, display_name, role
        FROM users
        WHERE username = '${username}'
        AND password = '${password}'
        LIMIT 1
    `;

    try {

        const user = db.prepare(sql).get();

        if (!user) {
            return res.status(401).send(
                page(
                    "Authentication Failed",
                    `
                    <div class="error">
                        Invalid username or password.
                    </div>

                    <p>
                        <a href="/">Return to login</a>
                    </p>
                    `
                )
            );
        }

        req.session.user = {
            id: user.id,
            username: user.username,
            displayName: user.display_name,
            role: user.role
        };

        res.redirect("/dashboard");

    } catch (error) {

        console.error("Database query failed:", error.message);

        res.status(400).send(
            page(
                "Authentication Error",
                `
                <div class="error">
                    The portal could not process the authentication request.
                </div>

                <p>
                    <a href="/">Return to login</a>
                </p>
                `
            )
        );
    }
});

// ---------------------------------------------------------
// Authenticated researcher dashboard
// ---------------------------------------------------------

app.get("/dashboard", (req, res) => {

    if (!req.session.user) {
        return res.redirect("/");
    }

    const user = req.session.user;

    res.send(
        page(
            "Research Dashboard",
            `
            <div class="card">

                <h2>Welcome, ${user.displayName}</h2>

                <p>
                    Account:
                    <code>${user.username}</code>
                </p>

                <p>
                    Role:
                    ${user.role}
                </p>

            </div>


            <div class="card">

                <h2>Project Shadow — Incident Notes</h2>

                <div class="notice">

                    During the breach review, an encoded message
                    believed to have been left by the attacker was
                    recovered.

                    <br><br>

                    A copy has been placed in:

                    <br><br>

                    <code>/evidence/attacker-message.txt</code>

                    <br><br>

                    Initial analysis suggests that the message was
                    intentionally encrypted rather than merely encoded.

                </div>

                <p>
                    Incident reference:
                    <code>PS-IR-2026-03</code>
                </p>

            </div>


            <div class="card">

                <h2>Research Portal Access Confirmed</h2>

                <p>
                    Authentication to the compromised researcher
                    portal has been successfully reproduced.
                </p>

                <div class="flag">
                    ${FLAG}
                </div>

            </div>


            <p>
                <a href="/logout">Sign out</a>
            </p>
            `
        )
    );
});

app.get("/logout", (req, res) => {

    req.session.destroy(() => {
        res.redirect("/");
    });

});

app.listen(PORT, "0.0.0.0", () => {
    console.log(
        `Project Shadow PS-02 portal running on port ${PORT}`
    );
});
