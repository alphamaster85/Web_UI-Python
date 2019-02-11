$(function(){
    
    var selectedRadioActivities, selectedRadioSkills, text_number_Activities, text_number_Skills;
    function set_default() {
        selectedRadioActivities = null;
        selectedRadioSkills = null;
        text_number_Activities = 1;
        text_number_Skills = 1;
    };
    set_default();

    var text_stage_Activities = document.getElementById("tab_set_Activities").getElementsByTagName('p')[0].textContent;
    var text_stage_Skills = document.getElementById("tab_set_Skills").getElementsByTagName('p')[0].textContent;
    var targetActivities = document.getElementById("tab_set_Activities").querySelector("input:first-child");
    var targetSkills = document.getElementById("tab_set_Skills").querySelector("input:first-child");
    
    $("#set_Activities").prop("checked", true);
    $("#tab_set_Activities .stage_check:first-child").prop("checked", true);
    change_label_Activities(targetActivities, text_stage_Activities);

    function set_Activities(target) {
        set_previously_target()
        set_default()
        $("#tab_"+target.id+" .stage_check:first-child").prop("checked", true);
        text_stage_Activities = document.getElementById("tab_set_Activities").getElementsByTagName('p')[0].textContent;
        change_label_Activities(targetActivities, text_stage_Activities);
    };

    function set_Skills(target) {
        set_previously_target()
        set_default()
        $("#tab_"+target.id+" .stage_check:first-child").prop("checked", true);        
        text_stage_Skills = document.getElementById("tab_set_Skills").getElementsByTagName('p')[0].textContent;
        change_label_Skills(targetSkills, text_stage_Skills);
    };

    function check_Activities(target) {
        text_stage_Activities = $("#label_txt_"+target.id).html();
        change_label_Activities(target, text_stage_Activities);
    };

    function check_Skills(target) {
        text_stage_Skills = $("#label_txt_"+target.id).html();
        change_label_Skills(target, text_stage_Skills);
    };
    
    function change_label_Activities(target, text_stage) {
        set_previously_target()
        selectedRadioActivities = target;
        text_number_Activities = $("label[for='"+selectedRadioActivities.id+"']").html();
        $("label[for='"+selectedRadioActivities.id+"']").css("width", "15%");
        $("label[for='"+selectedRadioActivities.id+"']").html(text_stage); 
    
        stages = document.getElementsByClassName("stage_check_Activities");
        if (stages[0].checked) {
            $("#btn_prev_Activities").css("visibility", "hidden");
        } else {
            $("#btn_prev_Activities").css("visibility", "visible");
        };
    };

    function change_label_Skills(target, text_stage) {
        set_previously_target()
        selectedRadioSkills = target;
        text_number_Skills = $("label[for='"+selectedRadioSkills.id+"']").html();
        $("label[for='"+selectedRadioSkills.id+"']").css("width", "15%");
        $("label[for='"+selectedRadioSkills.id+"']").html(text_stage);
        
        stages = document.getElementsByClassName("stage_check_Skills");
        if (stages[stages.length-1].checked) {
            $("#btn_next_Skills").css("display", "none");
        } else {
            $("#btn_next_Skills").css("display", "block");
        };
    };

    function set_previously_target() {
        if (selectedRadioSkills) {
            $("label[for='"+selectedRadioSkills.id+"']").css("width", "4%");
            $("label[for='"+selectedRadioSkills.id+"']").html(text_number_Skills); 
        }
        if (selectedRadioActivities) {
            $("label[for='"+selectedRadioActivities.id+"']").css("width", "4%");
            $("label[for='"+selectedRadioActivities.id+"']").html(text_number_Activities); 
        }
    };

    $("#set_Activities").on("click", function(event) {
        set_Activities(event.target);
    });

    $("#set_Skills").on("click", function(event) {
        set_Skills(event.target);
    });
    
    $(".stage_check_Activities").on("click", function(event) {
        check_Activities(event.target);
    });

    $(".stage_check_Skills").on("click", function(event) {
        check_Skills(event.target);
    });

    var stages, index, ids;

    $("#btn_prev_Activities").on("click", function(event) {
        event.preventDefault();
        
        stages = document.getElementsByClassName("stage_check_Activities");
        ids = [];
        for (i = 0; i < stages.length; i++) {
            ids.push(stages[i].id);
            if (stages[i].checked) {
                index = i;
            };
        };
        if (index > 0) {
            $("#"+ids[--index]).prop("checked", true);            
            check_Activities(stages[index]);
        }; 
    });

    $("#btn_next_Activities").on("click", function(event) {
        event.preventDefault();

        stages = document.getElementsByClassName("stage_check_Activities");
        ids = [];
        for (i = 0; i < stages.length; i++) {
            ids.push(stages[i].id);
            if (stages[i].checked) {
                index = i;
            };
        };
        if (index < ids.length-1) {
            $("#"+ids[++index]).prop("checked", true);            
            check_Activities(stages[index]);
        } else if (index == ids.length-1) {
            $("#set_Skills").prop("checked", true);
            $("#tab_set_Skills .stage_check:first-child").prop("checked", true);
            set_Skills(stages[index]);
        };
    });

    $("#btn_prev_Skills").on("click", function(event) {
        event.preventDefault();

        stages = document.getElementsByClassName("stage_check_Skills");
        ids = [];
        for (i = 0; i < stages.length; i++) {
            ids.push(stages[i].id);
            if (stages[i].checked) {
                index = i;
            };
        };
        if (index > 0) {
            $("#"+ids[--index]).prop("checked", true);            
            check_Skills(stages[index]);
        } else if (index == 0) {
            $("#set_Activities").prop("checked", true);
            // $("#tab_set_Activities .stage_check:last-child").prop("checked", true);
            // set_previously_target();
            // set_default();
            stages = document.getElementsByClassName("stage_check_Activities");
            stages[stages.length-1].prop("checked", true);
            targetActivities = stages[stages.length-1];
            set_Activities(stages[stages.length-1]);
        };
    });

    $("#btn_next_Skills").on("click", function(event) {
        event.preventDefault();

        stages = document.getElementsByClassName("stage_check_Skills");
        ids = [];
        for (i = 0; i < stages.length; i++) {
            ids.push(stages[i].id);
            if (stages[i].checked) {
                index = i;
            };
        };
        if (index < ids.length-1) {
            $("#"+ids[++index]).prop("checked", true);            
            check_Skills(stages[index]);
        };
    });
});