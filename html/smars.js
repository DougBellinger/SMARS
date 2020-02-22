function debounced(delay, fn) {
  let timerId;
  return function (...args) {
    if (timerId) {
      clearTimeout(timerId);
    }
    timerId = setTimeout(() => {
      fn(...args);
      timerId = null;
    }, delay);
  }
}

const positions = [ 0, 90, 180, 270 ];
const commnads = ["RR", "FW", "RL", "RV"];
function move_handler(evt, data) {
  if (data.distance == 50) {
    var a = data.angle.degree;
    positions.forEach(function(p, index) {
    if (Math.min(Math.abs(a-p), Math.abs((360-a)-p)) < 20) {
      console.log ("position:", index);
        $.get("/command.php", { command: {F : 1} },  function(data){
          console.log(data);
        }).fail(function() {
          console.log("command failed");
        });
      }
    });
  }
}

function joystick_init() {
  var options = {
    position: {
      left: '50%',
      bottom: '50%'
    },
    mode: 'static',
    color: 'blue',
    threshold: 0.8,
    zone: document.getElementById('zone_joystick')
  };
  var manager = nipplejs.create(options);
  var joystick;

  manager.on('start', 
  function(evt, joystick) {
    joystick.off();
    joystick.on('move', debounced(500, move_handler));
    joystick.on('plain:up', function(evt, data) {
      // DO EVERYTHING
      console.log(evt);
    });
    joystick.on('plain:down', function(evt,data) {
      // DO EVERYTHING
      console.log(evt);
    });
    joystick.on('plain:left', function(evt,data) {
      // DO EVERYTHING
      console.log(evt);
    });
    joystick.on('plain:right', function(evt,data) {
      // DO EVERYTHING
      console.log(evt);
    });
    joystick.on('end', function(evt,data) {
      // DO EVERYTHING
      joystick.off('start move end dir plain');
      console.log(evt);
    });
  }).on('removed', function(evt, joystick) {
    joystick.off('start move end dir plain');
    delete joystick;
  });
}
