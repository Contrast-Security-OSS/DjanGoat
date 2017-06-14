node('docker') {
    stage ('checkout') {
        checkout scm
    }
    stage ('lint') {
        sh 'docker-compose run --rm python-lint'
    }
    stage('test') {
        sh 'docker-compose run --rm python-build'
    }
    stage('package'){
        sh 'docker-compose run --rm package'
        archiveArtifacts artifacts: '*zip'
    }
    stage ('cleanup') {
         sh 'docker-compose down'
    }
}