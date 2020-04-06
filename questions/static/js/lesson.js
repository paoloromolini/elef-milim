let correct_answsers = 0;
let result = $('#result');
let success = $('#success');
$('#submit').on('click', function(event){
    event.preventDefault();
    correct_answsers = 0;
    $( ".question" ).each(function() {
        let id = $(this).attr('id');
        let answer = $( this ).val().toLowerCase();
        let correctAnswers = dict[id]['correct'];
        let correctGender = dict[id]['gender'];
        let gender_input = 'gender-' + id;
        genderIsCorrect = true;
        if (correctGender != 'None') {
            genderIsCorrect = $("input[name="+gender_input+"]:checked"). val() == correctGender;
        }
        if (correctAnswers.indexOf(answer) >= 0 && genderIsCorrect) {
            $(this).removeClass('border-danger');
            $(this).addClass('border-success');
            correct_answsers++;
        } else {
            $(this).removeClass('border-success');
            $(this).addClass('border-danger');
        };
    });

    success.hide();
    result.hide();
    if (correct_answsers === questions_count) {
        success.show();
    } else {
        result.show();
        result.html('<strong>Attenzione: </strong>' + correct_answsers + '/' + questions_count + ' risposte corrette.');
    }
});
$('#help').on('click', function(event){
    event.preventDefault();
    $( ".question" ).each(function() {
        let that = $(this);
        let id = that.attr('id');
        let hintA = dict[id]['correct']+'';
        that.val(hintA.split(',')[0]);
    });
});
