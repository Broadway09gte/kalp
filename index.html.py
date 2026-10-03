<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>I Love You - Dyline</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            background-color: #050002;
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            font-family: 'Georgia', serif;
        }
        canvas {
            display: block;
            max-width: 100%;
            max-height: 100%;
        }
    </style>
</head>
<body>

    <canvas id="heartCanvas"></canvas>

    <script>
        const canvas = document.getElementById('heartCanvas');
        const ctx = canvas.getContext('2d');

        // Ekran boyutunu telefonun çözünürlüğüne göre dinamik ayarlama
        function resizeCanvas() {
            const size = Math.min(window.innerWidth, window.innerHeight, 600);
            canvas.width = size;
            canvas.height = size;
        }
        resizeCanvas();
        window.addEventListener('resize', resizeCanvas);

        // Kalp katman ayarları (Ekrana tam sığması için responsive scale)
        const katmanlar = [
            { scale: 0.58, adim: 55, renk: "#ffb6c1", boyut: 9 },  // En dış
            { scale: 0.48, adim: 48, renk: "#ff69b4", boyut: 9 },  // Orta dış
            { scale: 0.38, adim: 40, renk: "#ff1493", boyut: 8 },  // Orta iç
            { scale: 0.28, adim: 32, renk: "#c71585", boyut: 8 }   // En iç
        ];

        let theta = 0;
        const step = 0.015; // Yağ gibi akan dönüş hızı

        // Parametrik kalp denklemi koordinatları
        function getHeartXY(angle, scale, center) {
            const x = 16 * Math.pow(Math.sin(angle), 3) * scale * (center / 16);
            // Canvas koordinatlarında Y ekseni aşağı doğru olduğu için eksi ile çarpıyoruz
            const y = -(13 * Math.cos(angle) - 5 * Math.cos(2 * angle) - 
                       2 * Math.cos(3 * angle) - Math.cos(4 * angle)) * scale * (center / 16);
            return { x: x + center, y: y + center };
        }

        function draw() {
            // Ekranı temizle ve mor-siyah opaklık ver (hafif kuyruk/glitch efekti için)
            ctx.fillStyle = "#050002";
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            const center = canvas.width / 2;

            // 1. DÖNEN "I LOVE YOU" DUVARI
            katmanlar.forEach(k => {
                ctx.fillStyle = k.renk;
                ctx.font = `bold ${k.boyut * (canvas.width / 600)}px Arial`;
                ctx.textAlign = "center";
                ctx.textBaseline = "middle";

                for (let i = 0; i < k.adim; i++) {
                    const angle = (i * (Math.PI * 2) / k.adim) + theta;
                    const pos = getHeartXY(angle, k.scale, center);
                    
                    ctx.save();
                    ctx.translate(pos.x, pos.y);
                    // Yazıların kalbin dönüş yönüne doğru hafifçe eğimli durması için
                    ctx.rotate(angle + Math.PI / 2); 
                    ctx.fillText("I love you", 0, 0);
                    ctx.restore();
                }
            });

            // 2. TAM MERKEZE SABİTLENMİŞ YAZILAR (M ♥ D / Dyline)
            const dynamicFont = canvas.width / 600; // Ekran küçüldükçe yazıları da küçültür
            
            // M Harfi
            ctx.fillStyle = "white";
            ctx.font = `bold ${36 * dynamicFont}px Georgia`;
            ctx.fillText("M", center - (40 * dynamicFont), center - (5 * dynamicFont));

            // Kırmızı Kalp Emojisi
            ctx.fillStyle = "#ff0844";
            ctx.font = `bold ${40 * dynamicFont}px Arial`;
            ctx.fillText("♥", center, center - (5 * dynamicFont));

            // D Harfi
            ctx.fillStyle = "white";
            ctx.font = `bold ${36 * dynamicFont}px Georgia`;
            ctx.fillText("D", center + (40 * dynamicFont), center - (5 * dynamicFont));

            // Dyline Yazısı
            ctx.fillStyle = "white";
            ctx.font = `bold ${22 * dynamicFont}px Georgia`;
            ctx.fillText("Dyline", center, center + (40 * dynamicFont));

            // Açıyı güncelle ve animasyonu sürdür
            theta += step;
            requestAnimationFrame(draw);
        }

        // Animasyonu başlat
        draw();
    </script>
</body>
</html>
