$(function(){

    // $(".stage_check").on("mouseover", function(event) {
    //     $(".stage_check label").css('background-color', '#e0f0e0');
    //     // $("label[for='"+this.id+"']").css('background', 'red');
    //     var text = $("label[for='"+this.id+"']").html();
    //     $("label[for='"+this.id+"']").html(text+'0');   
    // });
        
    var selectedRadio;
    $(".stage_check").on("click", function(event) {
        var target = event.target;
        var text_old = $("label[for='"+this.id+"']").html();
        var text_new = $("#label_txt_"+this.id).html();
        console.log('old ' + text_old);
        console.log('new ' + text_new);
        change_txt(target, text_new);
    });
    function change_txt(node, text) {
        console.log('Click');
        if (selectedRadio) {
            $("label[for='"+selectedRadio.id+"']").html(text); 
        }
        selectedRadio = node;
        $("label[for='"+selectedRadio.id+"']").html('99'); 
    };


    $("#btn_prev_Activities").on("click", function(event) {
        event.preventDefault();
        console.log('Click');
        // if (checkInput(inputMin)) {
        //     $("#inputMin").removeClass("typeError");
        //     $("#error").attr("hidden", "");
        //     $("#error").html("");
        // } 
    });

    $("#btn_next_Activities").on("click", function(event) {
        event.preventDefault();

        console.log('Click');
    });

    $("#btn_prev_Skills").on("click", function(event) {
        event.preventDefault();

        console.log('Click');
    });

    $("#btn_next_Skills").on("click", function(event) {
        event.preventDefault();

        console.log('Click');
    });
});