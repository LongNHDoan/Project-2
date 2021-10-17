var vg_1 = "worldCo2Map.vl.json";
var vg_2 = "industryCo2.vl.json";
var vg_3 = "worldCo2LineChart.vl.json";
var vg_4 = "annualIndustryCo2AreaChart.vl.json";
var mapButtn = document.getElementById("mapBtn");
var lineButtn = document.getElementById("lineBtn");

vegaEmbed("#world", vg_1, { "actions": false }).then(function (result) { }).catch(console.error);
vegaEmbed("#industry1", vg_2, { theme: "urbaninstitute", "actions": false }).then(function (result) { }).catch(console.error);
vegaEmbed("#industry2", vg_4, { theme: "urbaninstitute", "actions": false }).then(function (result) { }).catch(console.error);

mapButtn.onclick = function () {
    vegaEmbed("#world", vg_1).then(function (result) { }).catch(console.error);
};
lineButtn.onclick = function () {
    vegaEmbed("#world", vg_3, { theme: "urbaninstitute", "actions": false }).then(function (result) { }).catch(console.error);
};
