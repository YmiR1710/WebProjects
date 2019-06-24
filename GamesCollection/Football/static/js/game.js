let cvs = document.getElementById("canvas");
let ctx = cvs.getContext("2d");

let ball = new Image();
let player = new Image();
let field = new Image();
let gates = new Image();

ball.src = "static/images/ball.png";
player.src = "static/images/player.png";
field.src = "static/images/field.png";
gates.src = "static/images/gates.png";

let xPos_player = 124;
let yPos_player = 350;
let xPos_gates = 200 * Math.random();
let yPos_gates = 0;
let xPos_ball = 250 * Math.random();
let yPos_ball = 100;
let score = 0;

let physic = {
    left_down : function(){xPos_ball -=4; yPos_ball +=4;},
    right_down : function(){xPos_ball +=4; yPos_ball +=4;},
    left_up : function(){xPos_ball -=4; yPos_ball -=4;},
    right_up : function(){xPos_ball +=4; yPos_ball -=4;},
    curr : Math.floor(Math.random() * 2)
};

let curr_func = function(){physic.curr === 1 ? physic.right_down() : physic.left_down();};

document.addEventListener("keydown", function(event) {
    xPos_player <= 0 && event.which === 37 ? xPos_player += 0: xPos_player >= 252 && event.which === 39
        ? xPos_player += 0 : xPos_player += event.which === 39 ? 8 : event.which === 37 ? -8 : 0
});

draw = function () {
    ctx.drawImage(field, 0, 0);
    ctx.drawImage(player, xPos_player, yPos_player);
    ctx.drawImage(ball, xPos_ball, yPos_ball);
    ctx.drawImage(gates, xPos_gates, yPos_gates);
    curr_func();
    if(xPos_ball <= 0 && physic.curr === 2){
        curr_func = function(){physic.right_up()};
        physic.curr = 3;
    }
    else if(xPos_ball <= 0 && physic.curr === 0){
        curr_func = function(){physic.right_down()};
        physic.curr = 1;
    }
    else if(xPos_ball >= 252 && physic.curr === 1){
        curr_func = function(){physic.left_down()};
        physic.curr = 0;
    }
    else if(xPos_ball >= 252 && physic.curr === 3){
        curr_func = function(){physic.left_up()};
        physic.curr = 2;
    }
    else if(xPos_player + player.width >= xPos_ball && xPos_ball + ball.width >= xPos_player &&
        yPos_player + player.height >= yPos_ball && yPos_ball + ball.height >= yPos_player){
        if(physic.curr === 1){
            curr_func = function(){physic.right_up()};
            physic.curr = 3;
        }
        else{
            curr_func = function(){physic.left_up()};
            physic.curr = 2;
        }
    }
    else if(yPos_ball <= 56 && !(xPos_gates + gates.width >= xPos_ball && xPos_ball + ball.width >= xPos_gates)){
        if(physic.curr === 2){
            curr_func = function(){physic.left_down()};
            physic.curr = 0;
        }
        else{
            curr_func = function(){physic.right_down()};
            physic.curr = 1;
        }
    }
    else if(xPos_gates + gates.width >= xPos_ball && xPos_ball + ball.width >= xPos_gates && yPos_ball <=35){
        if(physic.curr === 2){
            curr_func = function(){physic.left_down()};
            physic.curr = 0;
        }
        else{
            curr_func = function(){physic.right_down()};
            physic.curr = 1;
        }
        score++;
    }
    document.getElementById("score").textContent = "Score: " + score;
    yPos_ball >= 467 ? location.reload() :
        requestAnimationFrame(draw);
};
gates.onload = draw;
