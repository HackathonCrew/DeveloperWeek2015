var clientApp = angular.module('clientApp', []);


//Do dynamic angular stuff
clientApp.controller('ClientController', ['$scope', '$http', function($scope, $http){
    $scope.clicked = false;

    $http.get('/api/get_statement')
        .success(function(data, status, headers, config){
            $scope.politicians = data;
        });

    $http.get('/api/get_party_array')
        .success(function(data, status, headers, config){
            $scope.party = data.party;
            // console.log(p)
        });

    $scope.reloadPage = function(){
        window.location.reload();
    }

    $scope.selectParty = function(){
        if (!$scope.clicked){
            $scope.clicked = true;
        }
        else{
            $scope.clicked = false;
        }
    }


}]);

clientApp.filter('capitalize', function() {
    return function(input, scope) {
        if (input!=null)
        input = input.toLowerCase();
        return input.substring(0,1).toUpperCase()+input.substring(1);
    }
});

clientApp.directive('selectParty', function(){
    var link = function(scope, element, attrs) {
        element.bind('mousedown', function(){
            element.addClass('liked');
        })
    }
    return {
        restrict:"AE",
        link: link
    }
});
