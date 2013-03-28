$(document).ready(function(){

    var count = 2;

    var $addCall = $('#addCall');
    var $textGroup = $('#textGroup');
    var $about = $('#about');
    var $aboutButton = $('#aboutButton');
    var $everythingElse = $('#everythingElse');

    $about.hide();

    $aboutButton.on('click', function(){
        if($everythingElse.is(":visible")){
            $everythingElse.fadeToggle('slow');
            setTimeout(function(){
                $about.fadeToggle('slow');
            }, 500);
        }else{
            $about.fadeToggle('slow');
            setTimeout(function(){
                $everythingElse.fadeToggle('slow');
            }, 500);
        }
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
