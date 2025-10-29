import type { PageLoad } from './$types';

export const load: PageLoad = async () => {
	const response = await fetch('http://localhost:5000/markers');
	return await response.json();
};
