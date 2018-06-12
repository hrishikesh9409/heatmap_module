// Generated by LiveScript 1.2.0
$(document).ready(function(){
  var hm;
  hm = h337.create({
    element: document.body,
    radius: 20,
    visible: true,
    opacity: 30
  });
  hm.store.generateRandomDataSet(400);
  hm.get('canvas').style.zIndex = 1;
  hm.get('canvas').onclick = function(e){
    return hm.store.addDataPoint(e.clientX, e.clientY, 100);
  };
  return hm.get('canvas').onmousemove = function(e){
    return hm.store.addDataPoint(e.clientX, e.clientY, 100);
  };
});