// include rabbit-ear
//ear.window = require("@xmldom/xmldom");
var myOrigami = ear.origami();
var svg = ear.svg(document.body, 600, 600);

svg.size(1, 1)
    .padding(0.1)
    .strokeWidth(1 / 100);

// start with an unfolded square
let origami = ear.origami();
var cp = ear.cp();

cp.segment(0, 0, 1, 1).valley();
cp.segment(0, 1, 1, 0).valley();
cp.segment(0, 0.5, 1, 0.5).mountain();
cp.segment(0.5, 0, 0.5, 1).mountain();
console.log("Hello world!");
//cp.segment(0.0, 1.0, 0.25, 0.75).valley();

// center square
//cp.rect(0.25, 0.25, 0.5, 0.5).valley();

// edge diagonals
//cp.segment(0.5, 0.0, 0.75, 0.25).mountain();
//cp.segment(1.0, 0.5, 0.75, 0.75).mountain();

svg.origami(cp);
svgExport.downloadSvg(
    // SVG ID
    svg,
    // File name
    "fold.svg",
    {  //custom size
      width: 200,
      height: 200
    }
 );
// // make an initial crease
// const startAngle = 2 + Math.random(); // radians
// const startCrease = ear.line.fromAngle(startAngle).translate(0.25, 0.25);
// origami.flatFold(startCrease);

// // every frame of onMove we fold the cache, not
// // the folded origami from the previous frame.
let cache = origami.copy();

svg.origami(origami.folded());

svg.onPress = () => { cache = origami.copy(); };
svg.onRelease = () => { cache = origami.copy(); };
svg.onMove = (mouse) => {
     if (mouse.buttons === 0) { return; }
     const crease = ear.axiom(2, {points: [mouse.press, mouse.position]}).shift();
     origami = cache.copy();
     origami.flatFold(crease);
     svg.removeChildren();
     svg.origami(origami.folded());

};