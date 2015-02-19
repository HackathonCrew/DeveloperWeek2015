var clientApp = angular.module('clientApp', ['ngSanitize']);


//Do dynamic angular stuff
clientApp.controller('ClientController', ['$scope', '$http', '$q', '$timeout', function($scope, $http, $q, $timeout){
    $scope.clicked = false;
    $scope.politician_array = [];
    $scope.correct = false;
    $scope.scoreTotal = 0;
    $scope.scoreCorrect = 0;
    $scope.scoreCorrectPercentage = 0;
    $scope.entities = [
    {
        "text": "Football Association",
            "docs_with_phrase": 115,
            "occurrences": 336,
            "docs_with_all_terms": 145,
            "cluster": 0
        }, {
            "text": "World Cup",
                "docs_with_phrase": 81,
                "occurrences": 754,
                "docs_with_all_terms": 95,
                "cluster": 0
    }];

    $scope.getData = function(){
        console.log('requesting new politician');

        promise = $http.get('/api/get_statement')
            .success(function(data, status, headers, config){
                console.log(data);
                $scope.politician_array.push(data);

                $scope.getData();
            });

        return promise;
    }

    $scope.getD3Bubble = function(){
        promise = $http.get('/api/get_d3')
            .success(function(data, status, headers, config){
                $scope.bubbleData = data;
            });
            return promise;
    }

    $scope.showNewQuote = function(){

        if ($scope.politician_array.length == 0)
        {
            var bubble = document.getElementById("bubble");
            $(bubble).addClass('animated');
            console.log('no politicians, waiting until we have another one')
            $scope.politician = undefined;
            $timeout($scope.showNewQuote, 100, true)
            return;
        }
        console.log('we have a politician, lets queue him up')
        console.log('oldpoli', $scope.politicians);
        $scope.politicians = $scope.politician_array[0];
        $scope.politician_array.shift();
        console.log('newpoli', $scope.politicians);
        $scope.clicked = false;
    }

    $scope.showPolitician = function(el)
    {
        $scope.clicked = true;
        var box = document.getElementById("box");

        var off_image = parseInt($('.politics').css('margin-left'));
        console.log("test", off_image);

        var facetop = $scope.politicians.text_offset.top;
        var faceleft = $scope.politicians.text_offset.left + off_image;
        var faceheight = $scope.politicians.text_offset.height;
        var facewidth = $scope.politicians.text_offset.width;

        $(box).css({top: facetop, left: faceleft, height: faceheight, width: facewidth});

        var bubble = document.getElementById("bubble");
        var leftoffset = $scope.politicians.text_offset.offset[0] + off_image;
        var bottomoffset = $scope.politicians.text_offset.offset[1] + 220;
        $(bubble).css({bottom: bottomoffset, left: leftoffset});
        $(bubble).addClass('animated');

        $scope.scoreTotal += 1;
        if (el == $scope.politicians.party){
            $scope.correct = true;
            $scope.scoreCorrect += 1;
        }else{
            $scope.correct = false;
        }
        $scope.scoreCorrectPercentage = Math.floor(($scope.scoreCorrect / $scope.scoreTotal) * 100.0);
    }

    $http.get('/api/get_party_array')
        .success(function(data, status, headers, config){
            $scope.party = data.party;
        });
}]);

clientApp.filter('capitalize', function() {
    return function(input, scope) {
        if (input!=undefined)
        {
            input = input.toLowerCase();
            return input.substring(0,1).toUpperCase()+input.substring(1);
        }else {
            return "";
        }
    }
});

clientApp.directive('bubbleChart', function($parse, $window){
    return{
        restrict: 'EA',
        template:"<svg width='250' height='50'></svg>",
        link: function(scope, elem, attrs){
            var exp = $parse(attrs.entities);
            console.log('ext', scope.entities);
            var entities = scope.entities; //exp(scope);

            json = {
                "name": "flare",
                "children": []
            };

            clusters = {};
            for (var i = 0; i < entities.length; i++) {
                entity = entities[i];
                console.log('entity:' + entity);
                entity = {
                    "name": entity.text,
                    "size": entity.occurrences
                };
                cluster = clusters[entities[i].cluster];
                if (cluster) {
                    clusters[entities[i].cluster].children.push(entity);
                } else(
                clusters[entities[i].cluster] = {
                    "name": i + "",
                        "children": [entity]
                });
            }

            for (var o in clusters) {
                json.children.push(clusters[o]);
            }

            var r = 160, //960
                format = d3.format(",d"),
                fill = d3.scale.category10();

            var bubble = d3.layout.pack()
                .sort(null)
                .size([r, r])
                .padding(0.5); //1.5

            var vis = d3.select("#chart").append("svg")
                .attr("width", r)
                .attr("height", r)
                .attr("class", "bubble");

            var node = vis.selectAll("g.node")
                .data(bubble.nodes(classes(json))
                .filter(function (d) {
                return !d.children;
            }))
                .enter().append("g")
                .attr("class", "node")
                .attr("transform", function (d) {
                return "translate(" + d.x + "," + d.y + ")";
            });

            node.append("title")
                .text(function (d) {
                return d.className + ": " + format(d.value);
            });

            node.append("circle")
                .attr("r", function (d) {
                return d.r;
            })
                .style("fill", function (d) {
                return fill(d.packageName);
            });

            node.append("text")
                .attr("text-anchor", "middle")
                .attr("dy", ".3em")
                .text(function (d) {
                return d.className.substring(0, d.r / 3);
            });

            // Returns a flattened hierarchy containing all leaf nodes under the root.
            function classes(root) {
                var classes = [];

                function recurse(name, node) {
                    if (node.children) node.children.forEach(function (child) {
                        recurse(node.name, child);
                    });
                    else classes.push({
                        packageName: name,
                        className: node.name,
                        value: node.size
                    });
                }

                recurse(null, root);
                return {
                    children: classes
                };
            }
        }
    }
});
