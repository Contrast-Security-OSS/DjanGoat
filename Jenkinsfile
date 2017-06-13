node('docker') {
    stage ('lint') {
        checkout scm
        sh 'docker-compose run --rm python-lint'
        }
    stage('test') {
        checkout scm
        sh 'docker-compose run --rm python-build'
    }
    stage('package'){
        checkout scm
        sh 'docker-compose run --rm package'
        archiveArtifacts artifacts: '*zip'
    }
    stage ('cleanup') {
         sh 'docker-compose down'
    }
}