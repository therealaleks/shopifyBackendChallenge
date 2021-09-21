import {Image} from 'react-bootstrap';

function ThumbNail({image}) {
    const content = image.content.content
    return(
        <a href={image.main_image} title={content.length>0 ? content.toString() : 'could not detect content'}>
            <Image 
            src={image.main_image} 
            className={'h-300 hover-zoom'}
            thumbnail
            />
        </a>);
}

export default ThumbNail;
