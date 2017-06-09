node('docker') {
    stage('test') {
        checkout scm
        sh 'docker-compose run --rm python'
        sh 'docker-compose down'
    }
}