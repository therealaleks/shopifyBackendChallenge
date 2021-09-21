import './App.css';
import{ useState, useRef } from 'react';
import { useAxios } from './configs/requests';
import {Image, Form, Button, Dropdown} from 'react-bootstrap';
import ThumbNail from './components/Thumbnail';
import uploadIcon from './ressources/upload.png';
import refreshIcon from './ressources/refresh.png';
import Select from 'react-select'
import qs from 'qs';

function App() { 
  const [files, setFiles] = useState(null);
  const [filterString, setFilters] = useState('');
  const [{ data }, get] =
  useAxios(
    {
      method: 'GET',
      url: '/image/'+filterString,
    },
  );

  const [{ loading: uploading}, upload] =
  useAxios(
    {
      method: 'POST',
      url: '/image/',
    },
    {
      manual: true,
    }
  );

  const [{ data: imgSearchData}, imgSearch] =
  useAxios(
    {
      method: 'POST',
      url: '/imageSearch/',
    },
    {
      manual: true,
    }
  );

  const filterOptions = [
    { value: 'Person', label: 'Person' },
    { value: 'Man', label: 'Man' },
    { value: 'Woman', label: 'Woman' },
    { value: 'Plant', label: 'Plant' },
    { value: 'Tree', label: 'Tree' },
    { value: 'Building', label: 'Building' },
    { value: 'Food', label: 'Food' },
    { value: 'Animal', label: 'Animal' },
    { value: 'Dog', label: 'Dog' },
    { value: 'Cat', label: 'Cat' },
    { value: 'Fruit', label: 'Fruit' },
    { value: 'Car', label: 'Car' },
  ];

  const handleUpload = (search = false) => {
    if (files) {
      let posts = [];
      Object.values(files).forEach(file => {
        const formData = new FormData();
        formData.append(
          "title",
          file.name,
        );
        formData.append(
          "main_image",
          file,
          file.name
        );
        if(search) {
          posts.push(imgSearch({
            data: formData,
          }));
        } else {
          posts.push(upload({
            data: formData,
          }));
        }
        
      });

      Promise.all(posts).then(get);
    }
    setFiles(null);
  };

  const handleUploadChange = (e) => {
    if(e.target.files?.length > 0)
      setFiles([...e.target.files]);
      e.target.value = null;
  };

  const handleFilterChange = (options) => {
    let filters = options.map((option) => option.value);

    const params = {
      content: JSON.stringify(filters),
    }

    setFilters(`?${qs.stringify(params)}`)

    get();
  };
  return (
    <div className="App">
      <h1> Simple Image Repo </h1>
      <div className='menu'>
        <Form.Control
          id="upload-photo"
          onChange={handleUploadChange}
          type="file" className='uploadbtn'
          hidden
        />
        {(imgSearchData) ? 
          <Image 
            src={refreshIcon}
            className='uploadButton'
            onClick={()=>window.location.reload()} 
          /> : 
          <>
            <label htmlFor="upload-photo">
              <Image src={uploadIcon} className='uploadButton'/>
            </label>
            {files ? files[0]?.name : 'No file selected'}
          </>
        }
        <div className='action'>
          <Button onClick={() => handleUpload(false)} variant="secondary">upload</Button>
          <Button onClick={() => handleUpload(true)} variant="secondary">search</Button>
        </div>
        <Select 
          options={filterOptions}
          className='filterSelector'
          placeholder='Select content filter categories'
          isMulti
          onChange={(options)=>handleFilterChange(options)}
        />
      </div>
      <div>
        {((imgSearchData) ? imgSearchData : data)?.map((image)=><ThumbNail key={image.main_image} image={image}/>)}
      </div>
    </div>
  );
}

export default App;
