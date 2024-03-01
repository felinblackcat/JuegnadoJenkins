node {
    def commited_email = sh(script: "git rev-parse HEAD",  returnStdout: true).trim()
    def commited_hash = sh(script: "git log -1 --format='%ae'",  returnStdout: true).trim()
    def coverage
    echo commited_email
    echo commited_hash
    stage("BuildTesting") {
        def customImage = docker.build("juegnadojenkins:latest")
        customImage.inside {
            sh "python --version"
        }
        coverage = sh(script: "docker run -w /var/jenkins_home/workspace/CI_CDtest_main --volumes-from 3a8d9b1a5e747074606855f78fa503260006fb9564d4e263bf39c8994a82b0a9 juegnadojenkins pytest --junitxml=./test.xml --cov=. --cov-fail-under=90 | grep TOTAL| awk '{print \$4}' | tr -d %", returnStdout: true).trim()
    }
    sh "ls /var/jenkins_home/workspace/CI_CDtest_main/"
    sh "ls /var/jenkins_home/workspace/CI_CDtest_main/app"
    echo coverage
    stage("CheckStaticCode") {
        echo "Hello, CheckStaticCode!"

    }
    stage("RunUnitaryTest") {
        echo "Hello, RunUnitaryTest!"
     }
    stage("BuildPreprod") {
        echo "Hello, BuildPreprod!"
    }
    stage("IntegrationTest") {
        echo "Hello, IntegrationTest!"
    }
    stage("CheckCVE") {
        echo "Hello, CheckCVE!"
    }
    stage("SendRegistry") {
        echo "Hello, SendRegistry!"

    }
    stage("UATDeploy") {
        echo "Hello, UAT Deploy!"
    }
    
}