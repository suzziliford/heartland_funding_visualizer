console.log("hello");

console.log(document);

let body = document.body;

console.dir(body);

let children = body.children;
console.log(children)

let container = children[0];
console.log(container);
console.dir(container);

// let cont2 = container.children[0];
console.log(pie);
console.dir(pie);

let butt = pie.children[0];
let butthole = butt.children[0];
console.log(butthole);

console.log(pieData)



function getInternational(){
    let response = fetch(`https://projects.propublica.org/nonprofits/api/v2/organizations/300739799.json`)
    response.json().then(data => {
        console.log(data)
    })
    // return data;
}


// async function getInternational(){
//     let response = await fetch(`https://projects.propublica.org/nonprofits/api/v2/organizations/300739799.json`)
//     let data = await response.json();
//     console.log(data)
//     // return data;
// }

fetch('https://projects.propublica.org/nonprofits/api/v2/organizations/300739799.json')
  .then(response => response.json())
  .then(data => {
    console.log(data);
  })
  .catch(error => {
    console.error('There was a problem with the fetch operation:', error);
  });



let twenty = document.getElementById('20');
let nineteen = document.getElementById('19');
let eighteen = document.getElementById('18');
let seventeen = document.getElementById('17');
let sixteen = document.getElementById('16');
let fifteen = document.getElementById('15');
let fourteen = document.getElementById('14');

// var ctx = document.getElementById("pie");
// console.log(ctx)



// twenty.addEventListener('mouseover', function(){
//     Promise.all([
//         fetch("https://projects.propublica.org/nonprofits/api/v2/organizations/300739799.json"),
//         fetch("https://projects.propublica.org/nonprofits/api/v2/organizations/363775696.json"),
//         fetch("https://projects.propublica.org/nonprofits/api/v2/organizations/361877640.json"),
//         fetch("https://projects.propublica.org/nonprofits/api/v2/organizations/36-4053244.json"),
//         fetch("https://projects.propublica.org/nonprofits/api/v2/organizations/36-3642952.json")
//     ])
//     .then(([res1, res2, res3, res4, res5]) => Promise.all([res1.json(), res2.json(), res3.json(), res4.json(), res5.json()]))
//     .then(([data1, data2, data3, data4, data5]) => {
//         console.log(data1)
//             const value1 = data1.filings_with_data[0].totrevenue;
//             const value2 = data2.filings_with_data[0].totrevenue;
//             const value3 = data3.filings_with_data[0].totrevenue;
//             const value4 = data4.filings_with_data[0].totrevenue;
//             const value5 = data5.filings_with_data[0].totrevenue;

//             let pieData = [
//                 {value: value1}, {value: value2}, {value: value3}, {value: value4}, {value: value5}
//             ]
            console.log(pieData)
//             new Chart(document.getElementById("chart").getContext("2d")).Pie(pieData);
//     })
//     .catch(error => console.error(error))
// });

twenty.addEventListener('mouseover', (e) => {console.log(e)});
twenty.addEventListener('mouseover', (e) => {changeGraph(e, "twenty")});

nineteen.addEventListener('mouseover', (e) => {console.log(e)});
nineteen.addEventListener('mouseover', (e) => {changeGraph(e, "nineteen")});


eighteen.addEventListener('mouseover', (e) => {console.log(e)});
eighteen.addEventListener('mouseover', (e) => {changeGraph(e, "eighteen")});


seventeen.addEventListener('mouseover', (e) => {console.log(e)});
seventeen.addEventListener('mouseover', (e) => {changeGraph(e, "seventeen")});

sixteen.addEventListener('mouseover', (e) => {console.log(e)});
sixteen.addEventListener('mouseover', (e) => {changeGraph(e, "sixteen")});

fifteen.addEventListener('mouseover', (e) => {console.log(e)})
fifteen.addEventListener('mouseover', (e) => {changeGraph(e, "fifteen")});

fourteen.addEventListener('mouseover', (e) => {console.log(e)})
fourteen.addEventListener('mouseover', (e) => {changeGraph(e, "fourteen")});



function changeGraph(e, year){
    let x;

    if (year === "twenty") {
        x = 0;
    } else if (year === "nineteen") {
        x = 1;
    } else if (year === "eighteen") {
        x = 2;
    } else if (year === "seventeen") {
        x = 3;
    } else if (year === "sixteen") {
        x = 4;
    } else if (year === "fifteen") {
        x = 5;
    } else if (year === "fourteen") {
        x = 6;
    }
    Promise.all([
        fetch("https://projects.propublica.org/nonprofits/api/v2/organizations/300739799.json"),
        fetch("https://projects.propublica.org/nonprofits/api/v2/organizations/363775696.json"),
        fetch("https://projects.propublica.org/nonprofits/api/v2/organizations/361877640.json"),
        fetch("https://projects.propublica.org/nonprofits/api/v2/organizations/36-3642952.json"),
        fetch("https://projects.propublica.org/nonprofits/api/v2/organizations/36-4053244.json"),
    ])
    .then(([res1, res2, res3, res4, res5]) => Promise.all([res1.json(), res2.json(), res3.json(), res4.json(), res5.json()]))
    .then(([data1, data2, data3, data4, data5]) => {
        console.log(data1)
            const value1 = data1.filings_with_data[x].totrevenue;
            const value2 = data2.filings_with_data[x].totrevenue;
            const value3 = data3.filings_with_data[x].totrevenue;
            const value4 = data4.filings_with_data[x].totrevenue;
            const value5 = data5.filings_with_data[x].totrevenue;

            let pieData = [
                {value: value1, label: 'International', color: "rgb(142, 235, 142)"},
                {value: value2, label: 'Health', color: "rgb(111, 156, 228)"},
                {value: value3, label: 'Human Needs and Rights', color: "rgb(144, 208, 237)"},
                {value: value4, label: 'Housing', color: "rgb(188, 164, 232)"},
                {value: value5, label: 'Care Services', color: "red"},
            ]


            var pieOptions = {
                animation: false
            }
            console.log(pieData)
            new Chart(document.getElementById("chart").getContext("2d")).Pie(pieData, pieOptions);
    })
    .catch(error => console.error(error));
};