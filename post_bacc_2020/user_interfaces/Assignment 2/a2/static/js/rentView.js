/*David A. Halloran, dh974@drexel.edu
CS530: DUI, Assignment 2*/

function RentViewer(numRows, bikesPerRow) {
    const that = this;

    const bikesPerPage = numRows * bikesPerRow;


    this.load = function () {
        $.get('/api/get_bikes', {
            n: numRows * bikesPerRow
        }, function (bikes) {
            that.update(bikes);
        });
    }


    this.update = function(bikes){
        $('#cards').empty();

        for (var row = 0; row < numRows; col++) {
            const deck = $('div class ="card deck"></div>');

            for (var col = 0; col < bikesPerRow; col++){
                const bike = bikes[row * bikesPerRow + col];

                const card = $(`
                    <div class="card">
                        <div class="card body">
                            <img class="card-img top="/static/img/bikes/${bike.image}">
                            <p class="card-title">${bike.name}</p>
                            <p class="card-title">${bike.avilable}</p>
                            <button class"less-button btn btn-primary">-</button>
                            <button class"more-button btn btn-primary">+</button>
                        </div>
                    </div>
                `);
                
                $(deck).append(card);
            }

            $('#cards').append(card);

        }

    }
}
