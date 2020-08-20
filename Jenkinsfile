pipeline {
    agent any
    
    options {
        ansiColor('xterm')
    }

    triggers {
        cron '''
        TZ=Asia/Seoul
        H 16 * * *
        '''
    }

    
    stages {

        // stage('DELETE CONTAINER') {
        //     steps {
        //         echo "✍️ CHECK CONTAINER EXIST"
        //         script{
        //             // 이전 빌드에 사용되었던 컨테이너를 삭제해준다.
        //             echo "DELETE LAST BUILD CONTAINER"
        //             def statuscode = sh script: "docker rm -f new-iris-e2e-$LAST_BUILD_NUMBER", returnStatus: true
        //             if (statuscode != 1 && statuscode != 0){
        //                 error "SOMETHING WRONG"
        //             }
        //             echo "END STAGE"
        //         }                
        //     }    
        // }

        stage('AUTO BUILD') {
            when {
                triggeredBy "TimerTrigger"
            }
            steps {
                echo "it is auto build ⏰"
                build(
                    job: 'minsoo-test',
                    wait: true,
                    parameters: [
                        string(name: 'build_target', value: 'IRIS-E2E-SAAS'),
                        string(name: 'menu_target', value: 'All'),
                        string(name: 'user', value: 'admin')
                        // string(name: 'container_number', value: "$BUILD_NUMBER")
                    ]
                )
            }
        }

        stage('PARAMS-E2E-TEST') {
            steps {
                echo "🔥 RUN PARAMETER E2E TEST"
                sh"""
                # 테스트 진행
                docker exec -t -w /root/IRIS-E2E-SAAS new-iris-e2e qa-script/run-e2e-headless-side.sh
                """
                echo "END STAGE"
            }    
        }
    }
    
}