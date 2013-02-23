$(document).ready(function(){

    var count = 2;

    var $addCall = $('#addCall');
    var $textGroup = $('#textGroup');
    var $about = $('#about');
    var $aboutButton = $('#aboutButton');

    $about.hide();

    $aboutButton.click(function(){
        $about.slideToggle('slow');
    });

    $addCall.click(function(){

        if(count<5){
            count++;
            $textGroup.append('<br>');
            $textGroup.append($('<input/>', {
                value: '',
                type: 'text',
                name: 'caller'+count,
                placeholder: 'Number '+count
            }));

            //To deal with the hidden fields I made
            $('hidden'+count).attr("name", "hidden"+count);

        }

    });

});
