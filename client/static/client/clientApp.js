var clientApp = angular.module('clientApp', ['ngSanitize']);


//Do dynamic angular stuff
clientApp.controller('ClientController', ['$scope', '$http', '$q', '$timeout', function($scope, $http, $q, $timeout){
    $scope.clicked = false;
    $scope.politician_array = [];
    $scope.correct = false;
    $scope.scoreTotal = 0;
    $scope.scoreCorrect = 0;
    $scope.scoreCorrectPercentage = 0;

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

    $scope.showNewQuote = function(){

        if ($scope.politician_array.length == 0)
        {

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
        var bottomoffset = $scope.politicians.text_offset.offset[1] + 250;
        $(bubble).css({bottom: bottomoffset, left: leftoffset});

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
