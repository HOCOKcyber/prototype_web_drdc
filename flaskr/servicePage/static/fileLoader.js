// Скрипт для загрузки файлов

let savedFiles = []
const fileInput = document.getElementById("file_upload")
const fileListDiv = document.getElementById("file_list") 

// Создание кнопки отчистки
const createdButton = document.createElement("button")
createdButton.innerText = "Отчистить все";
createdButton.onclick = clearAllFiles

// Добавляем файлы
fileInput.addEventListener("change", (event) => {
    const files = event.target.files
    savedFiles.push(...files)
    updateListView()
})

// Обовляем страницу
function updateListView(){
    if (savedFiles.length == 0){
        fileListDiv.innerHTML = ''
        return
    }

    // Если есть файлы
    fileListDiv.innerHTML = "Загруженные файлы:"
    
    savedFiles.forEach((file,index) => {
        const wrapper = document.createElement("div")
        wrapper.classList = "file_item_wrapper"
        
        const fileNameSpan = document.createElement("span")
        fileNameSpan.innerText = file.name

        const deleteFileButton = document.createElement("button")
        deleteFileButton.innerText = "×"
        deleteFileButton.classList = "delete_file"
        deleteFileButton.onclick = () => deleteFile(index)

        wrapper.appendChild(fileNameSpan)
        wrapper.append(deleteFileButton)
        fileListDiv.appendChild(wrapper)
    })

    fileListDiv.appendChild(createdButton)
}

// Удаляем все файлы
function clearAllFiles(){
    savedFiles = []
    updateListView()
}

// Удаляем конкретный файл
function deleteFile(index){
    savedFiles.splice(index, 1)
    updateListView()
}