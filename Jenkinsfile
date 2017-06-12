node('docker') {
    stage ('lint') {
        checkout scm
        sh 'docker-compose run --rm python-lint'
        }
    stage('test') {
        sh 'docker-compose run --rm python-build'
    }
    stage ('cleanup') {
         sh 'docker-compose down'
    }
}