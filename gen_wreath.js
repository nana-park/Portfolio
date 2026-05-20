const fs = require('fs');

function createWreath() {
    let leaves = '';
    const numLeaves = 14;
    // We create one branch on the left, from bottom to top
    // The spine is an arc from (x: 95, y: 130) to (x: 20, y: 20)
    for (let i = 0; i < numLeaves; i++) {
        const t = i / (numLeaves - 1);
        // Parametric curve for the spine (rough arc)
        const angle = -Math.PI/2 + (Math.PI * 0.4) * t; 
        const r = 80;
        const cx = 100;
        const cy = 100;
        
        const x = cx + r * Math.cos(angle);
        const y = cy + r * Math.sin(angle);
        
        // Tangent angle
        const tangent = angle + Math.PI/2;
        
        // Inner leaf
        const innerRot = (tangent - 0.4) * 180 / Math.PI;
        leaves += <path d="M0,0 C-10,-10 -20,-5 -25,5 C-15,10 -5,5 0,0" transform="translate(+x+,+y+) scale(0.6) rotate(+innerRot+)" fill="currentColor"/>;
        
        // Outer leaf
        const outerRot = (tangent + 0.4) * 180 / Math.PI;
        leaves += <path d="M0,0 C10,-10 20,-5 25,5 C15,10 5,5 0,0" transform="translate(+x+,+y+) scale(0.7) rotate(+outerRot+)" fill="currentColor"/>;
    }
    
    // Add stem
    leaves += <path d="M100,100 A80,80 0 0,0 20,20" fill="none" stroke="currentColor" stroke-width="2"/>;
    
    return <svg class="w-[200px] h-[160px] text-zinc-900 mb-2" viewBox="0 0 200 160" fill="none" xmlns="http://www.w3.org/2000/svg">
        <!-- Left Branch -->
        <g transform="translate(-10, -20)">
            \
        </g>
        <!-- Right Branch -->
        <g transform="translate(210, -20) scale(-1, 1)">
            \
        </g>
    </svg>;
}

let html = fs.readFileSync('index.html', 'utf8');

const regexGoogle = /<svg class="w-\[230px\] h-\[65px\] text-zinc-800 mb-2"[\s\S]*?<\/svg>/g;
const match = html.match(regexGoogle);
if (match) {
    const newSvg = createWreath();
    html = html.replace(match[0], newSvg).replace(match[1], newSvg);
    fs.writeFileSync('index.html', html, 'utf8');
    console.log("SVG replaced successfully.");
} else {
    console.log("SVG not found.");
}
