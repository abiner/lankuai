String.format = function () {
    if (arguments.length == 0)
        return null;
    var str = arguments[0];
    for (var i = 1; i < arguments.length; i++) {
        var re = new RegExp('\\{' + (i - 1) + '\\}', 'gm');
        str = str.replace(re, arguments[i]);
    }
    return str;
};

$(function () {
    $.ajax({
            type: 'POST',
            url: 'writeWorkList',
            data: {"parent": 100, "level": 1},

            success: function (data) {

                var all_ps = data['dict_city']
                for (var i = 0; i < all_ps.length; i++) {
                    var $html = String.format('<option value="{0}"> {1} </option>', all_ps[i][0], all_ps[i][1])
                    $('#Largefault').append($html)
                }
            },
            error: function (jqXHR, textStatus, errorThrown) {
                console.log("error");
            },
            dataType: 'json'
        }
    );
    $('#Largefault').change(function () {
        var parent = $('#Largefault').val();
        $.ajax({
            type: 'POST',
            url: 'writeWorkList',
            data: {"parent": parent, "level": 2},
            success: function (data) {
                var all_ps = data['dict_city'];
                var $shicode = $('#Smallfault').empty();
                $shicode.append('<option selected value="">请选择</option>')
                var $xiancode = $('#Faultdetailed').empty();
                $xiancode.append('<option selected value="">请选择</option>')
                for (var i = 0; i < all_ps.length; i++) {
                    var $html = String.format('<option value="{0}">{1}</option>', all_ps[i][0], all_ps[i][1])
                    $('#Smallfault').append($html)
                }
            },
            error: function (jqXHR, textStatus, errorThrown) {
                console.log("error");
            },
            dataType: 'json'
        });
    })

    $('#Smallfault').change(function () {
        var parent = $('#Smallfault').val()
        $.ajax({
            type: 'POST',
            url: 'writeWorkList',
            data: {"parent": parent, "level": 3},
            success: function (data) {
                var all_ps = data['dict_city']
                var $xiancode = $('#Faultdetailed').empty();
                $xiancode.append('<option selected value="">请选择</option>')
                for (var i = 0; i < all_ps.length; i++) {
                    var $html = String.format('<option value="{0}">{1}</option>', all_ps[i][0], all_ps[i][1])
                    $('#Faultdetailed').append($html)
                }
            },
            error: function (jqXHR, textStatus, errorThrown) {
                console.log("error");
            },
            dataType: 'json'
        });
    })
})