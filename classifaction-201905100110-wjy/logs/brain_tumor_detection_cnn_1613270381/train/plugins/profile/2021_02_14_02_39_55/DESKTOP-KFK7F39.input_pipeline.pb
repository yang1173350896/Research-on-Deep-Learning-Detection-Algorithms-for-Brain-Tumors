	NbX9??@NbX9??@!NbX9??@	/Uڂ????/Uڂ????!/Uڂ????"e
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails$NbX9??@?D???J??A?U?????@Y?_?L??*	33333?p@2F
Iterator::Model?ZӼ???!p????7U@)?MbX9??1*?????T@:Preprocessing2l
5Iterator::Model::ParallelMapV2::Zip[1]::ForeverRepeat?+e?X??!???ȳ!@)????<,??1??8|?o@:Preprocessing2v
?Iterator::Model::ParallelMapV2::Zip[0]::FlatMap[0]::Concatenate/?$???!f??c?`@)? ?	??1~`???@:Preprocessing2U
Iterator::Model::ParallelMapV2S?!?uq{?!?(>޼@)S?!?uq{?1?(>޼@:Preprocessing2Z
#Iterator::Model::ParallelMapV2::Zip#??~j???!~????A.@)??0?*x?1V/????@:Preprocessing2x
AIterator::Model::ParallelMapV2::Zip[1]::ForeverRepeat::FromTensora??+ei?!݌cS8???)a??+ei?1݌cS8???:Preprocessing2?
OIterator::Model::ParallelMapV2::Zip[0]::FlatMap[0]::Concatenate[0]::TensorSliceǺ???f?!????2???)Ǻ???f?1????2???:Preprocessing2f
/Iterator::Model::ParallelMapV2::Zip[0]::FlatMap??0?*??!V/????@)??_?LU?18?\{^??:Preprocessing:?
]Enqueuing data: you may want to combine small input data chunks into fewer but larger chunks.
?Data preprocessing: you may increase num_parallel_calls in <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map" target="_blank">Dataset map()</a> or preprocess the data OFFLINE.
?Reading data from files in advance: you may tune parameters in the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch size</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave cycle_length</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer_size</a>)
?Reading data from files on demand: you should read data IN ADVANCE using the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer</a>)
?Other data reading or processing: you may consider using the <a href="https://www.tensorflow.org/programmers_guide/datasets" target="_blank">tf.data API</a> (if you are not using it now)?
:type.googleapis.com/tensorflow.profiler.BottleneckAnalysis?
device?Your program is NOT input-bound because only 0.0% of the total step time sampled is waiting for input. Therefore, you should focus on reducing other time.no*no9/Uڂ????#You may skip the rest of this page.B?
@type.googleapis.com/tensorflow.profiler.GenericStepTimeBreakdown?
	?D???J???D???J??!?D???J??      ??!       "      ??!       *      ??!       2	?U?????@?U?????@!?U?????@:      ??!       B      ??!       J	?_?L???_?L??!?_?L??R      ??!       Z	?_?L???_?L??!?_?L??JCPU_ONLYY/Uڂ????b 