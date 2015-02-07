var clientApp = angular.module('clientApp', []);

//Do dynamic angular stuff
clientApp.controller('ClientController', ['$scope', '$http', function($scope, $http){

    $http.get('/api/get_statement')
        .success(function(data, status, headers, config){
            $scope.politicians = data;
            // console.log(data);
        });


}]);
