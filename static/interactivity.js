$(document).ready(function(){

    var count = 1;

    var $addCall = $('#addCall');
    var $textGroup = $('#textGroup');

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

        }

    });

});
