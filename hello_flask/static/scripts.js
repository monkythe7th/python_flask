
$(document).ready(function(){
    // $.ajax({
    //     type: 'GET',
    //     url: '/shopping/list',
    //     success:function(data){
    //         for (i in data) $('#shop__list').append('<li>'+data[i]+'</li>')
    //     }
    // })

    $('#shop__list--form').on('submit',function(e){
        e.preventDefault();
        $.ajax({
            type: 'POST',
            url:'/shopping/list',
            data:{
                item:$('#new__item').val()
            },
            success:function(data){
                $('#shop__list').append('<li>'+data[data.length - 1]+'</li>');
                console.log(data)
            }
        })
    });
});