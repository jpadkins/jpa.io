$ ->
    $('#sidebar h1').on 'click', ->
        window.location.href = $(this).attr('href')

    $('#sidebar h3').on 'click', ->
        window.location.href = $(this).attr('href')

    $('.article_list').on 'click', ->
        window.location.href = $(this).attr('href')
