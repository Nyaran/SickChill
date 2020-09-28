<%inherit file="../layouts/config.mako"/>
<%block name="css">
</%block>
<%block name="scripts">
    <script xmlns="http://www.w3.org/1999/html">
        $('#config-components').tabs();
    </script>
</%block>

<%block name="tabs">
    <li><a href="#anime-search">Search</a></li>
    <li><a href="#anidb-popular">Popular on AniDB</a></li>
</%block>

<%block name="saveButton">
</%block>

<%block name="pages">
    <div id="config-components">
        <div id="anime-search" class="component-group">
            <div class="row">
                <div class="col-lg-3 col-md-4 col-sm-4 col-xs-12">
                    <h3>${_('Search')}</h3>
                    <form method="post">
                        <div class="form-group">
                            <label for="query">${_('Query')}</label>
                            <input type="text" name="query" id="query" class="form-control input-sm input350" aria-describedby="queryHelp" autocapitalize="off" title="${_('Query')}" value="${query}"/>
                            <small id="queryHelp" class="form-text text-muted">${_('This can be a search string or an anime id from anidb')}</small>
                        </div>

                        <div class="form-group">
                            <label for="language">${'Adult'}</label>
                            <input type="checkbox" name="adult" id="adult"aria-describedby="adultHelp" title="${'Adult'}" value="${adult}">
                            <small id="adultHelp" class="form-text text-muted">${_('Check if you want to include adult anime in the results')}</small>
                        </div>
                        <div class="form-group">
                            <button type="submit" class="btn btn-primary">Submit</button>
                        </div>
                    </form>
                </div>
                <div class="col-lg-9 col-md-8 col-sm-8 col-xs-12">
                    % for result in search_results:
                        <div class="poster-container">
                            <div class="anime-container">
                                <div class="anime-image">
                                    <img
                                            src="${static_url("images/poster.png")}"
                                            data-src="${f'https://image.tmdb.org/t/p/w300_and_h450_bestv2{result["poster_path"]}'}"
                                            class="tvshowImg" alt="${_('Poster for')} ${result['title']} - ${result['release_date']}"
                                            onerror="this.src='${static_url("images/poster.png")}'"
                                    />
                                </div>
                                <div class="anime-information">
                                    <div class="anime-title">
                                        ${result['title'][0:34]}
                                    </div>

                                    <div class="anime-date">
                                        ${result['release_date']}
                                    </div>

                                    <div class="anime-details">
                                        <form method="post" action="${reverse_url('anime-add', 'add')}" class="form-horizontal pull-right">
                                            <input type="hidden" name="tmdb" value="${result['id']}">
                                            <button type="submit" class="btn btn-primary">Add</button>
                                        </form>
                                    </div>
                                </div>
                            </div>
                        </div>
                    % endfor
                </div>
            </div>
        </div>
    </div>
</%block>
