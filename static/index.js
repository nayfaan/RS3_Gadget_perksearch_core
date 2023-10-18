// function start_worker() {
//     if (typeof (Worker) !== "undefined") {
//         if (typeof (w) == "undefined") {
//             w = new Worker("./static/worker.js");
//         }
//         w.onmessage = function (event) {
//             if (event.data !== true) {
//                 var worker_result = event.data
//             }
//             else stop_worker();
//         };
//     }
// }

// function stop_worker() {
//     w.terminate();
//     w = undefined;
// }

//////////////////////////////////////////////////////////////////////////////////////////

var comps = {
    normal: {
        tool: ["null"],
        weapon: ["null"],
        armour: ["null"]
    },
    ancient: {
        tool: [],
        weapon: [],
        armour: []
    }
};

function distribute_comps(comp, comp_data, type){
    if (comp_data.tool.length > 0) comps[type].tool.push(comp);
    if (comp_data.weapon.length > 0) comps[type].weapon.push(comp);
    if (comp_data.armour.length > 0) comps[type].armour.push(comp);
}

for (var comp in data.comps) {
    var comp_data = data.comps[comp];
    if ('ancient' in comp_data) distribute_comps(comp, comp_data,"ancient")
    else distribute_comps(comp, comp_data, "normal")
}

// start_worker();
// w.postMessage(comps);

var level = 1;
var gizmo = ['normal', 'ancient'];

// var info = {
//     level: invLevelInput.getNumericValue(),
//     gizmo: gizmoSelect.findSelectedItem().getData().toLowerCase(),
//     materials: [
//         $(slotMiddle).attr('data-comp'),
//         $(slotTop).attr('data-comp'),
//         $(slotLeft).attr('data-comp'),
//         $(slotRight).attr('data-comp'),
//         $(slotBottom).attr('data-comp')
//     ],
//     ancient: ancientGizmo.isSelected(),
//     potion: potionSelect.findSelectedItem().getData().toLowerCase(),
//     shownoeffect: showProbType.isSelected()
// };

// var result = getMaterialsProb(info.levelwithpotion, info.gizmo, info.materials, info.ancient)
// self.dispResult(result, info)