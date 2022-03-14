//David A. Halloran, dh974@drexel.edu
//CS530: DUI, Assignment 3

class Grapher { //changed grapher from function to class so I can create the build method metioned in the pdf
    build(id){
        //creates the canvas object
        this.canvas = $(`<canvas id ="canvas"></canvas>`);
        $(id).append(this.canvas);
        this.bindElements();
        this.draw();

    }
    draw(){
        //function creates the grid, axis labels, and creates the graph curve
        var canvas = document.querySelector('canvas');
        canvas.width = 800;
        canvas.height = 500;
        var c = canvas.getContext('2d');
        c.font = "12px Helvetica"
        

        //x axis grid lines
        var x1 = 50;
        var x2 = 750;
        var y = 50;
        var i = 0;
        while(i < 13){
            c.beginPath();
            c.moveTo(x1, y);
            c.lineTo(x2, y);
            if(i == 6){
                c.strokeStyle = "black";
                c.lineWidth=2;
            }
            else{
                c.strokeStyle = "gray";
                c.lineWidth=1;
            }
            c.stroke();
            y += 35;
            i += 1;
        }

        //y axis grid lines
        var x = 50;
        var y1 = 50;
        var y2 = 470;
        var i = 0;
        while(i < 21){
            c.beginPath();
            c.moveTo(x, y1);
            c.lineTo(x, y2);
            if(i == 10){
                c.strokeStyle = "black";
                c.lineWidth=2;
            }
            else{
                c.strokeStyle = "gray";
                c.lineWidth=1;
            }
            c.stroke();
            x += 35;
            i += 1;
        }

        //implement axis labels
        //---> x labels
        var label = -10;
        var x = 40;
        var y = 275;
        while(label < 11){
            c.strokeStyle = "black";
            c.strokeText(label, x, y);
            x += 35
            label += 1;
        }

        //---> y labels
        var label = 6;
        var x = 385;
        var y = 55;
        while(label > -7){
            c.strokeStyle = "black";
            c.strokeText(label, x, y);
            y += 35
            label -= 1;
        }

        //Graph equation
        c.beginPath();
        c.strokeStyle = "blue";
        c.lineWidth=2;

        for(var i = 0; i < 700; i++){
            var x = pixelToX(i+50);
            var y = xToY(x);
            var yCoord = yToPixel(y);
            if(i === 0){
            c.moveTo(i+50, yCoord); 
            }
            else{
                c.lineTo(i+50, yCoord);
            }
        }
        c.stroke();
    }

    bindElements(){
        $("#a, #b, #c, #d").on("keyup", (event)=>{
            var inputVal = $(event.target).val();
            if(inputVal !== "" && !inputVal.match(/^[-,.,0-9]+$/)){
                if(inputVal !== "-"){
                    $(event.target).val(0);
                }
            }
            this.draw();
        });

        $("#canvas").on('mousemove', (event)=>{
            this.draw();
            var x = pixelToX(event.offsetX);
            var y = xToY(x);
            var yCoord = yToPixel(y);
            var canvas = document.querySelector('canvas');
            var c = canvas.getContext('2d');
            c.beginPath();
            c.rect(event.offsetX, yCoord, 70, 20)
            c.fillStyle = "green";
            c.fill();
            c.fillStyle = "white";
            c.fillText(`${Number.parseFloat(x).toPrecision(3)}, ${Number.parseFloat(y).toPrecision(3)}`, event.offsetX+5, yCoord+15);
        })
    }

}
function pixelToX(pixel){
    return (pixel-50)*(20/700)-10;
}

function xToY(x){
    var a_input = Number ($("#a").val()); 
    var b_input = Number ($("#b").val());
    var c_input = Number ($("#c").val());
    var d_input = Number ($("#d").val());
    return a_input*Math.pow(x, 3) + b_input*Math.pow(x, 2) + c_input*x + d_input
}

function yToPixel(y){
    return ((y*-1)+6)/(12/420)+50
}






