const axiosRequest = require('axios')

axiosRequest.get('https://httpstat.us/404')
    .then(res => {
        console.log(res.data.activity)
    })


async function getActivity() {
    try {
        let response = await axiosRequest.get('https://httpstat.us/500')
        console.log(`You could ${response.data.activity}`)
    } catch (error) {
        console.error(`ERROR: ${error}`)
    }
}



console.log("Exited at the end")