<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Deep Lab | Professional Trading Hub</title>
    <style>
        /* الأساسيات - Neo-Black Theme */
        :root {
            --neon-green: #39FF14;
            --deep-black: #050505;
            --glass-bg: rgba(10, 10, 10, 0.7);
            --text-gray: #888888;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Inter', -apple-system, sans-serif; }
        body { background-color: var(--deep-black); color: white; overflow-x: hidden; scroll-behavior: smooth; }

        /* خلفية الفيديو مع طبقة حماية (Overlay) */
        .hero {
            position: relative;
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
        }

        #bg-video {
            position: absolute;
            top: 50%; left: 50%;
            min-width: 100%; min-height: 100%;
            width: auto; height: auto;
            transform: translate(-50%, -50%);
            z-index: -2;
            filter: brightness(0.4);
        }

        .overlay {
            position: absolute;
            top: 0; left: 0;
            width: 100%; height: 100%;
            background: radial-gradient(circle, transparent 20%, var(--deep-black) 100%);
            z-index: -1;
        }

        /* المحتوى الرئيسي - Glassmorphism */
        .content {
            text-align: center;
            z-index: 1;
            padding: 40px;
            background: var(--glass-bg);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(57, 255, 20, 0.1);
            border-radius: 20px;
            max-width: 800px;
            animation: fadeIn 1.5s ease-out;
        }

        h1 {
            font-size: 4rem;
            letter-spacing: -2px;
            margin-bottom: 10px;
            font-weight: 800;
        }

        h1 span {
            color: var(--neon-green);
            text-shadow: 0 0 15px rgba(57, 255, 20, 0.3);
        }

        p.tagline {
            color: var(--text-gray);
            font-size: 1.2rem;
            letter-spacing: 2px;
            margin-bottom: 40px;
            text-transform: uppercase;
        }

        /* القفلة الاحترافية - Neo Style */
        .btn-access {
            display: inline-block;
            padding: 15px 45px;
            color: var(--neon-green);
            text-decoration: none;
            border: 1px solid var(--neon-green);
            border-radius: 5px;
            font-weight: bold;
            letter-spacing: 3px;
            transition: all 0.4s;
            background: transparent;
            position: relative;
        }

        .btn-access:hover {
            background: var(--neon-green);
            color: var(--deep-black);
            box-shadow: 0 0 30px rgba(57, 255, 20, 0.5);
            transform: translateY(-3px);
        }

        /* أقسام إضافية للشرح */
        .features {
            padding: 100px 5%;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
            background: var(--deep-black);
        }

        .card {
            padding: 40px;
            background: #0a0a0a;
            border: 1px solid #111;
            border-radius: 10px;
            transition: 0.3s;
        }

        .card:hover {
            border-color: var(--neon-green);
        }

        .card h3 { color: var(--neon-green); margin-bottom: 15px; font-size: 1.5rem; }
        .card p { color: var(--text-gray); line-height: 1.6; }

        /* أنيميشين */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @media (max-width: 768px) {
            h1 { font-size: 2.5rem; }
            .content { margin: 20px; }
        }
    </style>
</head>
<body>

    <section class="hero">
        <video autoplay muted loop id="bg-video">
            <source src="video.mp4" type="video/mp4">
        </video>
        <div class="overlay"></div>

        <div class="content">
            <h1>THE <span>DEEP</span> LAB</h1>
            <p class="tagline">Institutional Grade Trading Solutions</p>
            <a href="https://deeplab-terminal.streamlit.app" class="btn-access">ACCESS TERMINAL</a>
        </div>
    </section>

    <section class="features">
        <div class="card">
            <h3>Alpha Intelligence</h3>
            <p>Utilizing high-correlation data between NQ and QQQ to define institutional liquidity pools before 09:00 AM NY Open.</p>
        </div>
        <div class="card">
            <h3>Quant Execution</h3>
            <p>Custom-built analytics terminal for TradeLocker and proprietary firm tracking. Performance is measured by data, not emotions.</p>
        </div>
        <div class="card">
            <h3>Secure Ecosystem</h3>
            <p>Role-based access control for Mentors and Students, ensuring proprietary strategies remain within the lab.</p>
        </div>
    </section>

</body>
</html>
