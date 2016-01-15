$ ->
    $('#sidebar h3').on 'click', ->
        window.location.href = $(this).attr('href')
