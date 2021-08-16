//home section - catagories
let home_catagories = document.querySelector('.cat_list')

document.getElementById('cat_list').innerHTML = categoris.map(items =>
    `<div class="card home_cat">
                <div class="card-body">
                    <span class="couseIcons">${items.icons}</span>
                    <h4 class="card-title font-weight-bold pb-2">${items.title}</h4>
                    <p class="card-text pb-2">${items.details}</p>
                    <a href="/course">Read More ></a>
                </div>
            </div>`
).join('')